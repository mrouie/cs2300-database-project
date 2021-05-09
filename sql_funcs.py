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
        p1 = "insert into animal (cage_number,biological_class,species,"
        p2 = "feed_time,zoo_section,diet) values (?,?,?,?,?,?,?)"
        qry = p1 + p2
        animals = [(513,'Arachnida','Brazilian Black Tarantula','5PM','1A','Bugs'),
                   (204,'Reptile','American Alligator','12PM','4B','Meat')]
        curs.executemany(qry, animals)

def sample_employees(db_file):
  pass

def sample_managers(db_file):
  pass

def sample_caretakers(db_file):
  pass

def sample_takes_care_of(db_file):
  pass

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
    # user_input = input("Please enter the animal ID to find more info: ")
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        an1 = "select biological_class,species,zoo_section,diet,feed_time"
        an2 = " from animal where aid = " + aid
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
        print(zname + "'s hours are: " + business_hours)

def add_animal(db_file, animals):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into animal (cage_number,biological_class,species,feed_time,zoo_section,diet) values (?,?,?,?,?,?);"
        curs.executemany(qry,animals)
        
def update_animal(db_file,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if cage_num != 0:
            qry = "update animal set cage_number = " + cage_num + " where aid = " + aid
            curs.execute(qry)
        elif bio_class != 0:
            qry = "update animal set biological_class = " + bio_class + " where aid = " + aid
            curs.execute(qry)
        elif species != 0:
            qry = "update animal set species = " + species + " where aid = " + aid
            curs.execute(qry)
        elif feed_time != 0:
            qry += "update animal set feed_time = " + feed_time + " where aid = " + aid
            curs.execute(qry)
        elif zoo_sec != 0:
            qry = "update animal set zoo_section = " + zoo_sec + " where aid = " + aid
            curs.execute(qry)
        elif diet != 0:
            qry += "update animal set diet = " + diet + " where aid = " + aid
            curs.execute(qry)

def delete_animal(db_file, aid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from animal where aid = " + aid
        curs.execute(qry)

def all_employees(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select fname,eid,zname from employee"
        
        curs.execute(qry)
        
        headers = ["Name","ID","Zoo Name"]
        print(tabulate(curs.fetchall(), headers))

def add_employee(db_file, employees):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into employee (fname,minit,lname,phone_number,s_date,sex,age,salary,zname) values (?,?,?,?,?,?,?,?,?);"
        curs.executemany(qry,employees)

def update_employee(db_file, eid):
    pass

def delete_employee(db_file, eid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from employee where eid = " + eid
        curs.execute(qry)

def add_manager(db_file, eid):
    pass

def update_manager(db_file, eid):
    pass

def delete_manager(db_file, eid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from manager where eid = " + eid
        curs.execute(qry)

def add_caretaker(db_file, eid, zoo_sub):
    pass

def update_caretaker(db_file, eid, zoo_sub):
    pass

def delete_caretaker(db_file, eid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from caretaker where eid = " + eid
        curs.execute(qry)

def is_manager(db_file, eid):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select eid from mananger"
        curs.execute(qry)
        if eid in curs.fetchall():
            return True
        else:
            return False

db_file = "zoo.db"
schema_file = "zoo_schema.sql"

db_exists = os.path.exists(db_file)

if not db_exists:
    with sqlite3.connect(db_file) as connector:
        with open(schema_file, 'rt') as f:
            schema = f.read()
        connector.executescript(schema)

if __name__ == "__main__":
    # animal_list = []
    # how_many = int(input("How many animal(s) would you like to add?: "))
    # for x in range(how_many):
    #     a = int(input("Please enter animal id: "))
    #     b = int(input("Please enter animal cage number: "))
    #     c = input("Please enter animal class: ")
    #     d = input("Please enter animal species: ")
    #     e = input("Please enter animal feed time: ")
    #     f = input("Please enter animal zoo section: ")
    #     g = input("Please enter animal diet: ")
    #     animal_list.append([a,b,c,d,e,f,g])
    # animals(db_file, animal_list)
    # all_animals(db_file)