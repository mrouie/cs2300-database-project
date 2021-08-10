import os, sys
import sqlite3

from tabulate import tabulate

def sample_zoo(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        p1 = "insert into zoo (zname, business_hours, phone_number, "
        p2 = "fax_number, email, loc_city, loc_state, loc_zip) "
        p3 = "values ('Zootopia', '8AM-5PM', 18005665622, 229991, 'zoo@gmail.com'"
        p4 = ", 'Chicago', 'Illinois', '65777');"
        qry = p1 + p2 + p3 + p4
        curs.execute(qry)

def sample_animals(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        p1 = "insert into animal (aid,cage_number,biological_class,species,"
        p2 = "feed_time,zoo_section,diet) values (?,?,?,?,?,?,?)"
        qry = p1 + p2
        animals = [(1,513,'Arachnida','Brazilian Black Tarantula','5PM','1A','Bugs'),
                   (2,515,'Arachnida','Brazilian Yellow Tarantula','4PM','1A','Bugs')]
        curs.executemany(qry, animals)

def all_animals(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select aid, cage_number, species from animal"
        
        curs.execute(qry)
        
        headers = ["ID","Cage Number","Species"]
        print(tabulate(curs.fetchall(), headers))

def zoo_info(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select zname, business_hours, phone_number, "
        s2 = "fax_number, email, loc_city, loc_state, loc_zip from zoo"
        select = s1 + s2
        curs.execute(select)

def animal_info(db_file, aid):
    # user_input = input("Please enter the animal ID to find out more info: ")
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        an1 = "select biological_class,species,zoo_section,diet,feed_time"
        an2 = " from animal where aid = " aid
        qry = an1 + an2
        
        curs.execute(qry)
        
        headers = ["Class","Species","Zoo Section","Diet","Feed Time"]
        print(tabulate(curs.fetchall(), headers))
        
def zoo_times(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select zname, business_hours from zoo"
        curs.execute(qry)
        zname, business_hours = curs.fetchone()
        print("The zoo", zname)

def animals(db_file, animals):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into animal (aid,cage_number,biological_class,species,feed_time,zoo_section,diet) values (?,?,?,?,?,?,?);"
        curs.executemany(qry,animals)

def is_manager(db_file, eid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select eid from mananger"
        curs.execute(qry)
        curs.fetchall()

db_file = "zoo.db"
schema_file = "zoo_schema.sql"

db_exists = os.path.exists(db_file)

if not db_exists:
    with sqlite3.connect(db_file) as connector:
        with open(schema_file, 'rt') as f:
            schema = f.read()
        connector.executescript(schema)

if __name__ == "__main__":
    animal_list = []
    how_many = int(input("How many animal(s) would you like to add?: "))
    for x in range(how_many):
        a = int(input("Please enter animal id: "))
        b = int(input("Please enter animal cage number: "))
        c = input("Please enter animal class: ")
        d = input("Please enter animal species: ")
        e = input("Please enter animal feed time: ")
        f = input("Please enter animal zoo section: ")
        g = input("Please enter animal diet: ")
        animal_list.append([a,b,c,d,e,f,g])
    animals(db_file, animal_list)
    all_animals(db_file)
