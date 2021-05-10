import os, sys
import sqlite3

from tabulate import tabulate

def sample_zoo(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        p1 = "insert into zoo (zname, business_hours, phone_number, "
        p2 = "fax_number, email, loc_city, loc_state, loc_zip) "
        p3 = "values ('Zootopia', '8AM-5PM', 18005665622, 229991, 'zoo@gmail.com'"
        p4 = ", 'Chicago', 'Illinois', '65777');"
        qry = p1 + p2 + p3 + p4
        curs.execute(qry)

def sample_animals(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        p1 = "insert into animal (cage_number,biological_class,species,"
        p2 = "feed_time,zoo_section,diet) values (?,?,?,?,?,?)"
        qry = p1 + p2
        animals = [(513,'Arachnida','Brazilian Black Tarantula','5PM','B4','Bugs'),
                   (204,'Reptile','American Alligator','12PM','A1','Meat')]
        curs.executemany(qry, animals)

def sample_employees(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into employee (fname,minit,lname,phone_number,s_date,sex,age,salary) values (?,?,?,?,?,?,?,?)"
        employees = [('John','L','Doe','3144565689','10-21-09','M','32','$3200/month'),('Alex','Q','Wachter','4172238937','05-24-01','M','25','$5000/month')]
        curs.executemany(qry, employees)

def sample_managers(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into manager (eid,zoo_subsection) values (?,?)"
        managers = [('1','A1')]
        curs.executemany(qry, managers)

def sample_caretakers(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into caretaker (eid,zoo_subsection,specialty) values (?,?,?)"
        caretakers = [('2','A1','Reptiles')]
        curs.executemany(qry, caretakers)

def sample_takes_care_of(db_file): # Sample values to test database
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into takes_care_of (eid, aid) values (?,?)"
        ids = [['2','2']]
        curs.executemany(qry, ids)

def zoo_info(db_file): # Accesses zoo table to display zoo info
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select zname, business_hours, phone_number, "
        s2 = "fax_number, email, loc_city, loc_state, loc_zip from zoo"
        select = s1 + s2
        curs.execute(select)

def animal_info(db_file, aid): # Accesses animal table to display animal info for a specific animal
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        an1 = "select biological_class,species,zoo_section,diet,feed_time"
        an2 = " from animal where aid = " + aid
        qry = an1 + an2
        
        curs.execute(qry)
        
        headers = ["Class","Species","Zoo Section","Diet","Feed Time"]
        print(tabulate(curs.fetchall(), headers))
        
def zoo_times(db_file): # Accesses zoo table to display zoo hours.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select zname, business_hours from zoo"
        curs.execute(qry)
        zname, business_hours = curs.fetchone()
        print(zname + "'s hours are: " + business_hours)

def all_animals(db_file): # Prints entirety of animal table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select aid, cage_number, species from animal"
        curs.execute(qry)
        headers = ["ID","Cage Number","Species"]
        print(tabulate(curs.fetchall(), headers))

def add_animal(db_file, animals): # Takes a list of lists of animal values to be inputted into the database.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into animal (cage_number,biological_class,species,feed_time,zoo_section,diet) values (?,?,?,?,?,?);"
        curs.executemany(qry,animals)
        
def update_animal(db_file,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet):
# From the menu, takes a new value from one of the above variables and updates the corresponding table entry with that value.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if cage_num != 0:
            qry = "update animal set cage_number =" + cage_num + " where aid =" + aid
            curs.execute(qry)
        elif bio_class != 0:
            qry = "update animal set biological_class =\"" + bio_class + "\" where aid =" + aid
            curs.execute(qry)
        elif species != 0:
            qry = "update animal set species =\"" + species + "\" where aid =" + aid
            curs.execute(qry)
        elif feed_time != 0:
            qry = "update animal set feed_time =\"" + feed_time + "\" where aid =" + aid
            curs.execute(qry)
        elif zoo_sec != 0:
            qry = "update animal set zoo_section =\"" + zoo_sec + "\" where aid =" + aid
            curs.execute(qry)
        elif diet != 0:
            qry = "update animal set diet =\"" + diet + "\" where aid =" + aid
            curs.execute(qry)

def delete_animal(db_file, aid): # Given the animal id, deletes its entry in the table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from animal where aid = " + aid
        curs.execute(qry)

def all_employees(db_file): # Prints entirety of employee table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select fname,lname,eid from employee"
        curs.execute(qry)
        headers = ["First Name","Last Name","ID"]
        print(tabulate(curs.fetchall(), headers))

def add_employee(db_file, employees): # Takes a list of lists of employee values to be inputted into the database.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into employee (fname,minit,lname,phone_number,s_date,sex,age,salary) values (?,?,?,?,?,?,?,?);"
        curs.executemany(qry,employees)

def update_employee(db_file,eid,fname,minit,lname,pn,s_date,sex,age,salary):
# From the menu, takes a new value from one of the above variables and updates the corresponding table entry with that value.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if fname != 0:
            qry = "update employee set fname = \"" + fname + "\" where eid = " + eid
            curs.execute(qry)
        elif minit != 0:
            qry = "update employee set minit = \"" + minit + "\" where eid = " + eid
            curs.execute(qry)
        elif lname != 0:
            qry = "update employee set lname = \"" + lname + "\" where eid = " + eid
            curs.execute(qry)
        elif pn != 0:
            qry = "update employee set phone_number = " + pn + " where eid = " + eid
            curs.execute(qry)
        elif s_date != 0:
            qry = "update employee set s_date = \"" + s_date + "\" where eid = " + eid
            curs.execute(qry)
        elif sex != 0:
            qry = "update employee set sex = \"" + sex + "\" where eid = " + eid
            curs.execute(qry)
        elif age != 0:
            qry = "update employee set age = " + age + " where eid = " + eid
            curs.execute(qry)
        elif salary != 0:
            qry = "update employee set salary = \"" + salary + "\" where eid = " + eid
            curs.execute(qry)

def delete_employee(db_file, eid): # Given the employee id, deletes its entry in the table, as well as the tables of caretaker/manager if they exist.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from employee where eid = " + eid
        curs.execute(qry)

def avg_employee_age(db_file): # Sums and averages employee's ages
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select age from employee"
        curs.execute(qry)
        counter = 0
        age_total = 0
        for age in curs.fetchall():
            age_total += age[0]
            counter += 1
        print()
        print("The average age of employees' is:", (age_total/counter))
        print()

def max_employee_age(db_file): # Finds the max value in the employee table for age.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select age from employee"
        curs.execute(qry)
        temp = 0
        for age in curs.fetchall():
            if age[0] > temp:
                temp = age[0]
        print()
        print("The oldest employee is:", temp)
        print()

def min_employee_age(db_file): # Finds the min value in the employee table for age.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select age from employee"
        curs.execute(qry)
        temp = 150
        for age in curs.fetchall():
            if age[0] < temp:
                temp = age[0]
        print()
        print("The youngest employee is:", temp)
        print()

def total_animal_count(db_file): # 
     with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select aid from animal"
        curs.execute(qry)
        count = 0
        for aid in curs.fetchall():
            count += 1
        print()
        print("There are", count, "animals in the zoo.")
        print()


def all_managers(db_file): # Prints entirety of manager table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select eid,zoo_subsection from manager"
        curs.execute(qry)
        headers = ["ID","Zoo Subsection"]
        print(tabulate(curs.fetchall(), headers))

def add_manager(db_file, managers): # Takes a list of lists of manager values to be inputted into the database.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into manager (eid,zoo_subsection) values (?,?);"
        curs.executemany(qry,managers)

def update_manager(db_file,eid,zoo_sub):
# From the menu, takes a new value for zoo_sub and updates its entry based on the employee id.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "update manager set zoo_subsection = \"" + zoo_sub + "\" where eid = " + eid
        curs.execute(qry)

def delete_manager(db_file, eid): # Given the employee id, deletes its entry in the table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from manager where eid = " + eid
        curs.execute(qry)

def all_caretakers(db_file): # Prints entirety of manager table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select eid,zoo_subsection,specialty from caretaker"
        curs.execute(qry)
        headers = ["ID","Zoo Subsection","Specialty"]
        print(tabulate(curs.fetchall(), headers))

def add_caretaker(db_file, caretakers): # Takes a list of lists of caretaker values to be inputted into the database.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into caretaker (eid,zoo_subsection,specialty) values (?,?,?);"
        curs.executemany(qry,caretakers)

def update_caretaker(db_file, eid, zoo_sub, specialty):
# From the menu, takes a new value for zoo_sub or specialty and updates its entry based on the employee id.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if zoo_sub != 0:
            qry = "update caretaker set zoo_subsection = \"" + zoo_sub + "\" where eid = " + eid
            curs.execute(qry)
        elif specialty != 0:
            qry = "update caretaker set specialty = \"" + specialty + "\" where eid = " + eid
            curs.execute(qry)

def delete_caretaker(db_file, eid): # Given the employee id, deletes its entry in the table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from caretaker where eid = " + eid
        curs.execute(qry)

def all_takes_care_of(db_file): # Prints entirety of takes_care_of table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select eid,aid from takes_care_of"
        curs.execute(qry)
        headers = ["Employee ID","Animal ID"]
        print(tabulate(curs.fetchall(), headers))

def add_takes_care_of(db_file, ids): # Takes a list of lists of id values to be inputted into the database.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into takes_care_of (eid,aid) values (?,?);"
        curs.executemany(qry,ids)

def delete_takes_care_of(db_file, eid, aid): # Given the employee id AND animal id, deletes its entry in the table.
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "delete from takes_care_of where eid = " + eid + " and aid = " + aid
        curs.execute(qry)

def is_manager(db_file, eid): # Checks the list of ids in the manager table to determine if the eid in the parameter is a manager.
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

db_exists = os.path.exists(db_file) # Checks to see if a database file already exists.

if not db_exists: # Creates a new database file with the schema read from the sql file if there isn't already a database file.
    with sqlite3.connect(db_file) as connector:
        with open(schema_file, 'rt') as f:
            schema = f.read()
        connector.executescript(schema)

if __name__ == "__main__":
     pass