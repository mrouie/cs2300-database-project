# Hello
# sahbarwal more like cyberwal
"""
Some kind of documentation
"""

import os, sys
import sqlite3
from getpass import getpass

import sql_funcs

USERS_FILE = "users.txt"
ADMINS_FILE = "admins.txt"


# Zoo Database Class 
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

        accounts = users_file.read().splitlines()
        admin_usernames = admins_file.read().splitlines()

        for user, admin in zip(accounts, admin_usernames):
            username, password = user.split(sep=":", maxsplit=2)

            if username not in self.users.keys():
                self.users[username] = password
            if username in admin_usernames:
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
        username = input("Enter your username:\nZooDatabase> ")
        if username == "":
            return False
        print()
        password = getpass("Enter your password:\nZooDatabase> ")

        if username in self.users:
            if self.users[username] == password:
                self.is_logged_in = True
                self.current_user = username
            else:
                print("Incorrect password.")
                return False

            if username in self.admins.keys():
                self.is_admin = True

            return True

        else:
            return False







# Login Menu Function
def menu_login(zoo):
    choice = "TBD"
    while(choice != 'q'):
        print("Welcome to The Zookepers!")
        print("1. Login to an existing account.")
        print("2. Sign up a new account.")
        print("3. Forgot password.")
        print("q. Quit")

        choice = input("ZooDatabase> ")
        if choice == '1':
            zoo.login()

            if not zoo.is_logged_in:
                print("Login failed.")
                zoo.login()
            else:
                return menu_main(zoo)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            pass

# Main Menu Function 
def menu_main(zoo):
    choice = 'TBD'
    options_user = {
        '1': "View all animals.",
        '2': "View a map of the Zoo",
        '3': "Find more information about a specific animal.",
        '4': "Find the Zoo's Open Hours.",
        '5': "Find info about the Founders of the Zookeepers Zoo.",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    options_admin = {
        '1': "View all animals.",
        '2': "View a map of the Zoo",
        '3': "Find more information about a specific animal.",
        '4': "Find the Zoo's Open Hours.",
        '5': "Find info about the Founders of the Zookeepers Zoo.",
        '6': "Manage animal(s)",
        '7': "Manage employee(s)",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    while(choice != 'q' and choice != 'quit'):
        print("Please choose from the options below: ")
        if zoo.is_admin:
            for option, desc in options_admin.items():
                if desc is not None:
                    print(option + ". " + desc)
            choice = input("ZooDatabase> ")
            if choice not in options_admin.keys():
                print("Invalid choice. Choose from the options below:")
                continue
        else:
            for option, desc in options_user.items():
                if desc is not None:
                    print(option + ". " desc)
            choice = input("ZooDatabase> ")
            if choice not in options_admin.keys():
                print("Invalid choice. Choose from options below:")
                continue
        
        if choice == '1':
            sql_funcs.all_animals()
        elif choice == '2':
            # zoo.view_map() #TODO: pls implement
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            menu_animal()
        elif choice == '7':
            menu_manager()



        else:
            choice = input("ZooDatabase> ")
            while(choice not in options_user):
                choice = input("INVALID INPUT. Please enter a valid input. Any input other than 1, 2, 3, 4, 5, or q is invalid.\nZooDatabase> ")

        # Additional Admin Options
        else:
            print("6. : ")
            print("7. : ")
            print("8. : ")
            print("9. : ")
            print("10. : ")
            print("11.: ")
            print("12. : ")
            print("13. : ")
            print("q. Log out: ")
            choice = input("ZooDatabase> ")
            while(choice not in options_admin):
                choice = input("INVALID INPUT. Please enter a valid input. Any input other than 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 or q is invalid.\nZooDatabase> ")
    
    return choice

def menu_animal():
    choice = "NO CHOICE"
    options = {
        '1': "Add an animal.",
        '2': "Update an animal.",
        '3': "Remove an animal.",
        '4': "Go back.",
        'q': "Quit.",
    }
    while(choice != 'q'):
        
        print("What would you like to do?")
        for x in options:
            print options[x]
        
        choice = input()

        if choice == '1':
            animals = []
            how_many = int(input("How many animals would you like to add?: "))
            for x in range(how_many):
                a = int(input("Please enter animal id: "))
                b = int(input("Please enter animal cage number: "))
                c = input("Please enter animal class: ")
                d = input("Please enter animal species: ")
                e = input("Please enter animal feed time: ")
                f = input("Please enter animal zoo section: ")
                g = input("Please enter animal diet: ")
                animals.append([a,b,c,d,e,f,g])
            sql_funcs.animals(db_file, animals)
            
                
        elif choice == '2':
            update_choice = "TBD"
            continue_choice = 'yes'
            animal_options = {
                '1': "The animal's id.",
                '2': "The animal's cage number.",
                '3': "The animal's class.",
                '4': "The animal's species.",
                '5': "The animal's feeding time.",
                '6': "The animal's zoo section.",
                '7': "The animal's diet.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            } 
            while(update_choice.lower() == 'yes'):
                print("What information about the animal would you like to update?")
                for x in aniaml_options:
                    print animal_options[x]
                update_choice = input()
                # NOT SURE AS TO HOW I ACCESS THE ANIMAL INFO SO THIS IS PSEUDO CODE
                if update_choice == '1':
                    animal.id = int(input())
                elif update_choice == '2':
                    animal.cage_number == int(input())
                elif update_choice == '3':
                    animal.classs == input()
                elif update_choice == '4':
                    animal.species == input()
                elif update_choice == '5':
                    animal.feed_time == input()
                elif update_choice == '6':
                    animal.zoo_section == input()
                elif update_choice == '7':
                    animal.diet == input() 
                elif update_choice == 'b' or update_choice == 'back':
                    menu_animal()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the animal?(yes or no)")

        # I DO NOT SEE A REMOVE ANIMAL FUNCTION SO I GUESS WHEN YOU GUYS WRITE IT YOU CAN EDIT THIS OPTION
        elif choice == '3':
            pass
        elif choice == '4':
            menu_main(zoo)
        elif choice == 'q' or choice == 'quit':
            exit()
        


def menu_manager():
    choice = "NO CHOICE"
    options = {
        '1': "Add a manager.",
        '2': "Add a caretaker.",
        '3': "Update a manager.",
        '4': "Update a caretaker.",
        '5': "Remove a manager.",
        '6': "Remove a caretaker.",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    while(choice != 'q'):   

        print("What would you like to do?")
        for x in options:
            print options[x]
        
        choice = input()
    
        if choice == '1':
            manager = []
            how_many = int(input("How many managers would you like to add?: "))
            for x in range(how_many):
                a = input("Please enter the manager's name: ")
                a = int(input("Please enter", a + "'s id: "))
                b = int(input("Please enter", a + "'s age: "))
                c = input("Please enter", a + "'s phone number: ")
                d = input("Please enter", a + "'s salary: ")
                e = input("Please enter", a + "'s starting date: ")
                f = input("Please enter", a + "'s zoo subsection: ")
                manager.append([a,b,c,d,e,f])
            sql_funcs.manager(db_file, manager)       
        elif choice == '2':
            caretaker = []
            how_many = int(input("How many caretakers would you like to add?: "))
            for x in range(how_many):
                a = input("Please enter the caretaker's name: ", x)
                a = int(input("Please enter", a + "'s id: "))
                b = int(input("Please enter", a + "'s age: "))
                c = input("Please enter", a + "'s phone number: ")
                d = input("Please enter", a + "'s salary: ")
                e = input("Please enter", a + "'s starting date: ")
                f = input("Please enter", a + "'s specialty: ")
                caretaker.append([a,b,c,d,e,f])
            sql_funcs.caretaker(db_file, caretaker) 
        elif choice == '3':
            update_choice = "TBD"
            continue_choice = 'yes'
            manager_options = {
                '1': "The manager's name.",
                '2': "The manager's id.",
                '3': "The manager's age.",
                '4': "The manager's phone number.",
                '5': "The manager's salary.",
                '6': "The manager's starting date.",
                '7': "The manager's zoo subsection.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            } 
            while(update_choice.lower() == 'yes'):
                print("What information about the manager would you like to update?")
                for x in manager_options:
                    print manager_options[x]
                update_choice = input()
                # NOT SURE AS TO HOW I ACCESS THE MANAGER'S INFO SO THIS IS PSEUDO CODE
                if update_choice == '1':
                    manager.name = input()
                elif update_choice == '2':
                    manager.id == int(input())
                elif update_choice == '3':
                    manager.age == int(input())
                elif update_choice == '4':
                    manager.phone_number == input()
                elif update_choice == '5':
                    manager.salary == input()
                elif update_choice == '6':
                    manager.starting_date == input()
                elif update_choice == '7':
                    manager.zoo_subsection == input()
                elif update_choice == 'b' or update_choice == 'back':
                    menu_manager()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the manager?(yes or no)")
        elif choice == '4':
            update_choice = "TBD"
            continue_choice = 'yes'
            caretaker_options = {
                '1': "The caretaker's name.",
                '2': "The caretaker's id.",
                '3': "The caretaker's age.",
                '4': "The caretaker's phone number.",
                '5': "The caretaker's salary.",
                '6': "The caretaker's starting date.",
                '7': "The caretaker's specialty.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            } 
            while(update_choice.lower() == 'yes'):
                print("What information about the caretaker would you like to update?")
                for x in caretaker_options:
                    print caretaker_options[x]
                update_choice = input()
                # NOT SURE AS TO HOW I ACCESS THE CARETAKER'S INFO SO THIS IS PSEUDO CODE
                if update_choice == '1':
                    caretaker.name = input()
                elif update_choice == '2':
                    caretaker.id == int(input())
                elif update_choice == '3':
                    caretaker.age == int(input())
                elif update_choice == '4':
                    caretaker.phone_number == input()
                elif update_choice == '5':
                    caretaker.salary == input()
                elif update_choice == '6':
                    caretaker.starting_date == input()
                elif update_choice == '7':
                    caretaker.specialty == input()
                elif update_choice == 'b' or update_choice == 'back':
                    menu_manager()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the caretaker?(yes or no)")
        
        # I DO NOT SEE A REMOVE ANIMAL FUNCTION SO I GUESS WHEN YOU GUYS WRITE IT YOU CAN EDIT OPTIONS 5 AND 6
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == 'b' or choice == 'back':
            menu_main(zoo)
        elif choice == 'q' or choice == 'quit':
            exit()

    
def menu_view_users():
    pass

if __name__ == "__main__":
    zoo = ZooDatabase()
    zoo.load_users(USERS_FILE, ADMINS_FILE)
    # db_file = "zoo.db"
    user_choice = ""

    print("Welcome " + zoo.current_user + " to your Zoo Access Terminal.")
    while(user_choice != "quit" and user_choice != "q"):
        user_choice = menu_login(zoo)














