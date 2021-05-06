# Hello
# sahbarwal more like cyberwal
"""
Some kind of documentation
"""

import os, sys
import sqlite3
from getpass import getpass


USERS_FILE = "users.txt"
ADMINS_FILE = "admins.txt"



class ZooDatabase:
    def __init__(self):
        self.users: dict = {}
        self.admins: dict = {}

        self.is_logged_in = False
        self.is_admin = False
        self.current_user = ""

    def load_users(self, user_filename, admins_filename):
        users_file = open("users.txt", "r")
        admins_file = open("admins.txt", "r")

        accounts = users_file.readlines()
        admin_accts = admins_file.readlines()

        for user in accounts:
            username, password = user.split(sep=":", maxsplit=2)
            password = password.replace("\n", "")

            if username not in self.users.keys():
                self.users[username] = password
            if username in admin_accts:
                self.admins[username] = password
        
        users_file.close()
        admins_file.close()
        
        print(self.users)
        print(self.admins)
    
    def create_user(self, username, password):
        users_file = open("users.txt", "a")
        users_file.write(username + ":" + password + "\n")
        users_file.close()

    def make_admin(self, username):
        if username not in self.users:
            raise RuntimeError("Username does not exist.")
        else:
            admins_file = open("admins.txt", "a")
            admins_file.write(username)
            admins_file.close()


    def login(self):
        self.is_logged_in = False
        username = input("Enter your username: ")
        if username == "":
            return False
        
        password = getpass("Enter your password: ")

        if username in self.users:
            if self.users[username] == password:
                self.is_logged_in = True
                self.current_user = username
            else:
                print("Incorrect password.")
                return False

            if username in self.admins:
                self.is_admin = True

            return True

        else:
            return False
        
'''
class Zoo:
    def __init__(self):
        self.name = "The ZooKeepers"
        self.business_hours = []
        self.phone_number = 3145678901
        self.email = "help@thezookeepers.com"
        self.fax = 3147894561
        self.city = "Rolla"
        self.state = "Missouri"

        self.animals = []
        self.employees = []
        
    def add_animal(self, name, id_num, cage_num, population, diet, zoo_section, biological_class, image):
        New = Animal(name,id_num,cage_num, population, diet, zoo_section, biological_class, image)
        animals.append(New)
        
    def remove_animal(self,id_num):
        for i in range(len(animals)):
            if animals[i].id_num == id_num:
                animals.remove(i)





class Animal:
    def __init__(self):
        self.name = 'Unknown Animal'
        self.id_num = 0
        self.cage_num = 0
        self.population = 0
        self.diet: list = []
        self.zoo_section = 'Unknown Location'
        self.biological_class = 'Unknown'
        self.image = ''
    
    def __init__(self, name, id_num, cage_num, population, diet, zoo_section, biological_class):
        self.name = name
        self.id_num = id_num
        self.cage_num = cage_num
        self.population = population
        self.diet = diet
        self.zoo_section = zoo_section
        self.biological_class = biological_class




class Employee:
    def __init__(self):
        self.name = 'Unknown Worker'
        self.emp_id_num = 0
        self.phone_num = ''
        self.starting_date = ''
        self.sex = 'Unknown'
        self.age = 0
        self.salary = 0
'''

def menu_login():
    choice = ""
    while(choice != 'q'):
        print("Welcome to The Zookepers!")
        print("1. Login to an existing account.")
        print("2. Sign up a new account.")
        print("3. Forgot password.")
        print("q. Quit")

        if choice == 1:
            zoo.login()

            if not zoo.is_logged_in:
                print("Login failed.")
                zoo.login()

            choice = input()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            pass


def menu_main():
    while(choice != 'q'):
        print("Please choose from the options below:")
        print("1. View all animals: ")
        print("2. View a map of the Zoo: ")
        print("3. Find more information about a specific animal: ")
        print("4. Find the Zoo's Open Hours: ")
        print("5. Find info about the Founders of the Zookeepers Zoo: ")
    if user != admin:
        print("q - Log out: ")
    else:
        print("Please choose from the options below:")
        print("1. View all animals: ")
        print("2. View a map of the Zoo: ")
        print("3. Find more information about a specific animal: ")
        print("4. Find the Zoo's Open Hours: ")
        print("5. Find info about the Founders of the Zookeepers Zoo: ")
        print("6. Add animal(s): ")
        print("7. Add employee(s): ")
        print("8. Add manager(s): ")
        print("9. Promote an employee to a manager: ")
        print("10. Delete animal(s): ")
        print("11. Remove employee(s): ")
        print("12. Remove manager(s): ")
        print("13. Demote a manager to an employee: ")
        print("14. Log out: ")
    
def submenu():
    print("\n\n\n")
    return


    
def menu_view_users():
    pass

if __name__ == "__main__":
    zoo = ZooDatabase()
    zoo.load_users(USERS_FILE, ADMINS_FILE)

    menu_login()

    print("Welcome " + zoo.current_user + " to your Zoo Access Terminal.")
    while(choice.lower() != "quit" and choice.lower() != "q"):
        print("Please choose from the options below:")
        print("\"Login\": ")
        print("3. View all animals: ")
        print("4.  ")

        choice = input("ZooDatabase>")