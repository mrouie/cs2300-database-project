# Hello
# sahbarwal more like cyberwal
"""
Some kind of documentation
"""

import os, sys
import sqlite3
from getpass import getpass

import sql_funcs

DB_FILE = "zoo.db"
PROMPT = "ZooDatabase> "
USERS_FILE = "users.txt"
ADMINS_FILE = "admins.txt"


# Zoo Database Class 
class ZooDatabase:
    def __init__(self):
        self.users: dict = {} # key, value = username, password
        self.admins: dict = {} # (admins only) key, value = username, password

        self.is_logged_in = False # is the current user logged in
        self.is_admin = False # is the current user an admin
        self.current_user = "" # username of current user

    # loads all the users and admins from USERS_FILE and ADMINS_FILE
    def load_users(self, user_filename, admins_filename):
        users_file = open(USERS_FILE, "r") # each line should be formatted as username:password
        admins_file = open(ADMINS_FILE, "r") # each line should be a username that is an admin

        accounts = users_file.read().splitlines() # split each line of the users_file into a list of lines
        admin_usernames = admins_file.read().splitlines() # split each line of admins_usernames into a list of usernames

        users_file.close()
        admins_file.close()

        for user in accounts:
            username, password = user.split(sep=":", maxsplit=2) # splits username:password into two variables
            if username not in self.users.keys(): # prevent duplicate users
                self.users[username] = password
            if username in admin_usernames: # if it's an admin, add it to the list
                self.admins[username] = password
        return

    # creates and stores new user from std input into USERS_FILE
    def create_acct(self):
        print("Enter the username: ")
        username = input(PROMPT)
        if username in self.users.keys():
            print("That user already exists.")
            return False
        else:
            is_password_set = False
            while not is_password_set:
                print("Enter the password: ")
                password = getpass(PROMPT)
                if password == "":
                    return False
                print("Please confirm your password.")
                password_confirm = getpass(PROMPT)
                if password_confirm != password:
                    is_password_set = False
                    print("The passwords did not match. Try again.\n")
                else:
                    is_password_set = True
                    self.users[username] = password

        users_file = open("users.txt", "a")
        users_file.write(username + ":" + password + "\n")
        users_file.close()

        print(f"Welcome to TheZooKeepers {username}!")
        return True

    # Makes a user an admin from std input, current user must be an admin 
    def make_admin(self):
        if not self.is_admin:
            print("Insufficient permission. Only admins can make users admins.")
            return

        print("Enter the username of the user to make an admin: ")
        username = input(PROMPT)

        if username not in self.users:
            print("Username does not exist.")
            return

        admins_file = open("admins.txt", "a")
        admins_file.write(username)
        admins_file.close()
        return

    # Logs in a user with std input
    def login(self):
        self.is_logged_in = False # initialize failed login assumption
        print("Enter your username: ")
        username = input(PROMPT)

        if username in self.users and username != "":
            print("Enter your password: ")
            password = getpass(PROMPT)

            while self.users[username] != password:
                print("Incorrect password. Try again or enter nothing to cancel.")
                password = getpass()
                if password == "":
                    return False
            else:
                self.is_logged_in = True
                self.current_user = username

            if username in self.admins.keys():
                self.is_admin = True

            return True

        else:
            print("Username does not exist.")
            return False


# Function to add any key to continue. 
def waitKey():
    print("Press any key to continue...", end="")
    os.system('pause')
    print()

def clear_term():
    print(chr(27) + "[2J")

# Login Menu Function
def menu_login(zoo):
    choice = "TBD"
    while(choice != 'q'):
        clear_term()
        print("Welcome to The Zookepers!")
        print("1. Login to an existing account.")
        print("2. Sign up a new account.")
        print("q. Quit")

        # Branching to deal with user input
        choice = input(PROMPT)
        if choice == '1':
            zoo.login()
            
            # Branching to deal with Login failure
            if not zoo.is_logged_in:
                print("Login failed.")
                zoo.login()
            else:
                return menu_main(zoo)
                
        # Allows user to create a new account
        elif choice == '2':
            success = zoo.create_acct()
            if not success:
                print("User creation failed.")
        
        # Closes the Program once the user is finished
        elif choice == 'q' or choice == 'quit':
            exit()
        else:
            pass

# Main Menu Function 
def menu_main(zoo):
    clear_term()
    choice = 'TBD'

    # Tupples for the menu's that will be available to normal users and admins, respectively
    options_user = {
        '1': "View all animals.",
        '2': "View a map of the Zoo",
        '3': "Find more information about a specific animal.",
        '4': "Find the Zoo's Open Hours.",
        '5': "Find info about the Founders of the Zookeepers Zoo.",
        'b': "Go back.",
        'back': "",
        'q': "Exit.",
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
        '8': "Add/delete caretaker/animal relationship(s)",
        '9': "Various aggregrate functions",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    
    # Displays menu's for both normal users and admins
    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        if zoo.is_admin:
            for option, desc in options_admin.items():
                if option == 'b':
                    print('(b)ack' + ". " + desc)
                    continue
                if option == 'q':
                    print('(q)uit' + ". " + desc)
                    continue
                if option in ['back', 'quit']:
                    continue
                print(option + ". " + desc)
            choice = input(PROMPT)
            if choice not in options_admin.keys():
                print("Invalid choice. Choose from the options below:")
                continue
        else:
            for option, desc in options_user.items():
                if option == 'b':
                    print('(b)ack' + ". " + desc)
                    continue
                if option == 'q':
                    print('(q)uit' + ". " + desc)
                    continue
                if option in ['back', 'quit']:
                    continue
                print(option + ". " + desc)
            choice = input(PROMPT)
            if choice not in options_admin.keys():
                print("Invalid choice. Choose from options below:")
                continue  
        # Displays all animals
        if choice == '1':
            choice = "TBD"
            sql_funcs.all_animals(DB_FILE)
            waitKey()
        # Displays the map of the Zoo
        elif choice == '2':
            choice = "TBD"
            print_map()
            waitKey()
        # Displays info for a specific animal
        elif choice == '3':
            animal_to_find = input("Please enter the animal ID to find more info: ")
            if animal_to_find == "": 
                continue
            choice = "TBD"
            sql_funcs.animal_info(DB_FILE, animal_to_find)
            waitKey()
        # Displays Open Hours
        elif choice == '4':
            choice = "TBD"
            sql_funcs.zoo_times(DB_FILE)
            waitKey()
        # Displays Short Description about the Zoo Owners
        elif choice == '5'  :
            print("The Zookeepers Zoo was founded in 2021 by Mohammad Rouie, Ryland Chernesky, and Antonio Kotoni.")
            print("These 3 goons always had an addition to opening their own zoo; especially after seeing Professor Yeung's cats.")
            print("Not too long before 2021, these guys were strangers, but after going through the hardships of CS2300, they decided to drop out.")
            print("Their failure to code prorperly made them stronger than ever, and as a result they decided to create the Zookeepers Zoo.\n\n\n")
            waitKey()
        # Additional branching to show the added options admins should have
        if not zoo.is_admin:
            choice = input(PROMPT)
            while(choice not in options_user and choice != "TBD" and choice != ""):
                choice = input("INVALID INPUT. Please enter a valid input. Any input other than 1, 2, 3, 4, 5, or q is invalid.\n" + PROMPT)
        else:
            if choice == '6':
                choice = "TBD"
                menu_animal()
                waitKey()
            elif choice == '7':
                choice = "TBD"
                menu_manager()
                waitKey()
            elif choice == '8':
                choice = "TBD"
                menu_edit_relationship()
                waitKey()
            elif choice == '9':
                choice = "TBD"
                menu_aggregrate_functions()
                waitKey()
        
            while(choice not in options_admin and choice != "TBD" and choice != ""):
                choice = input("INVALID INPUT. Please enter a valid input. Any input other than 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 or q is invalid.\n" + PROMPT)
    
    return choice

# Function that prints map
def print_map():
    clear_term()
    maps = open("map.txt")
    lines = maps.read().splitlines()
    for line in lines:
        print(line)
    maps.close()
    

# Function that displays and deals with additional modifications to animals
def menu_animal():
    choice = "NO CHOICE"
    options = {
        '1': "Add an animal.",
        '2': "Update an animal.",
        '3': "Remove an animal.",
        'b': "Go back.",
        'q': "Quit.",
    }
    # Displays Menu
    while(choice != 'q'):
        clear_term()
        print("What would you like to do?")
        for option, desc in options.items():
            if option == 'b':
                print('(b)ack' + ". " + desc)
                continue
            if option == 'q':
                print('(q)uit' + ". " + desc)
                continue
            if option in ['back', 'quit']:
                continue
            print(option + ". " + desc)
        
        choice = input(PROMPT)
        
        # Deals with addition of Animals
        if choice == '1':
            animals = []
            how_many = int(input("How many animals would you like to add?:\n" + PROMPT))
            for x in range(how_many):
                a = int(input("Please enter animal cage number:\n" + PROMPT))
                b = input("Please enter animal class:\n" + PROMPT)
                c = input("Please enter animal species:\n" + PROMPT)
                d = input("Please enter animal feed time:\n" + PROMPT)
                e = input("Please enter animal zoo section:\n" + PROMPT)
                f = input("Please enter animal diet:\n" + PROMPT)
                animals.append([a,b,c,d,e,f])
            sql_funcs.add_animal(DB_FILE, animals)
        # Deals with updates to animals within the database based on ID       
        elif choice == '2':
            update_choice = "yes"
            animal_options = {
                '1': "The animal's cage number.",
                '2': "The animal's class.",
                '3': "The animal's species.",
                '4': "The animal's feeding time.",
                '5': "The animal's zoo section.",
                '6': "The animal's diet.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            aid = input("Which animal's info would you like to update?:\n" + PROMPT)
            while(update_choice.lower() == 'yes'):
                print("What information about the animal would you like to update?")
                for option, desc in animal_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                update_choice = input(PROMPT)

                cage_num,bio_class,species,feed_time,zoo_sec,diet = 0,0,0,0,0,0
                
                # Even more branching to deal with every possible demand for change in an animals attributes
                if update_choice == '1':
                    cage_num = input("Enter a new cage number:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == '2':
                    bio_class = input("Enter a new biological class:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == '3':
                    species = input("Enter a new species:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == '4':
                    feed_time = input("Enter a new feed time:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == '5':
                    zoo_sec = input("Enter a new zoo section:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == '6':
                    diet = input("Enter a new diet:\n" + PROMPT)
                    sql_funcs.update_animal(DB_FILE,aid,cage_num,bio_class,species,feed_time,zoo_sec,diet)
                elif update_choice == 'b' or update_choice == 'back':
                    menu_animal()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the animal?(yes or no)\n" + PROMPT)
        
        # Deletes an animal based on its ID
        elif choice == '3':
            aid = input("Please enter the animal's id to delete it:\n" + PROMPT)
            sql_funcs.delete_animal(DB_FILE, aid)
        # Goes back
        elif choice == 'b' or choice == 'back':
            return
        # Exits
        elif choice == 'q' or choice == 'quit':
            exit()
    

# Deals with the menu displayed to managers
def menu_manager():
    choice = "TBD"
    options = {
        '1': "Add an employee.",
        '2': "Add a manager.",
        '3': "Add a caretaker.",
        '4': "Update an employee.",
        '5': "Update a manager.",
        '6': "Update a caretaker.",
        '7': "Remove an employee.",
        '8': "Remove a manager.",
        '9': "Remove a caretaker.",
        '10': "View all employees.",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    # Displays menu
    while(choice not in ['b', 'back', 'q','quit']):
        clear_term()
        print("What would you like to do?")
        for option, desc in options.items():
            if option == 'b':
                print('(b)ack' + ". " + desc)
                continue
            if option == 'q':
                print('(q)uit' + ". " + desc)
                continue
            if option in ['back', 'quit']:
                continue
            print(option + ". " + desc)
        
        choice = input(PROMPT)
    
        # Adds employee
        if choice == '1':
            employees = []
            how_many = int(input("How many employees would you like to add?:\n" + PROMPT))
            for x in range(how_many):
                a = input("Please enter the employee's first name:\n" + PROMPT)
                b = input("Please enter " + a + "'s middle initial:\n" + PROMPT)
                c = input("Please enter " + a + "'s last name:\n" + PROMPT)
                d = input("Please enter " + a + "'s age:\n" + PROMPT)
                e = input("Please enter " + a + "'s phone number:\n" + PROMPT)
                f = input("Please enter " + a + "'s salary:\n" + PROMPT)
                g = input("Please enter " + a + "'s starting date:\n" + PROMPT)
                h = input("Please enter " + a + "'s zoo subsection:\n" + PROMPT)
                employees.append([a,b,c,d,e,f,g,h])
            sql_funcs.add_employee(DB_FILE, employees)
        # Branching that deals with all the possible changes to a manager
        elif choice == '2':
            managers = []
            how_many = int(input("How many managers would you like to add?:\n" + PROMPT))
            for x in range(how_many):
                a = input("Please enter the employee's id:\n" + PROMPT)
                b = input("Please enter the zoo subsection to manage:\n" + PROMPT)
                managers.append([a,b])
            sql_funcs.add_manager(DB_FILE, managers)
        # Branching that deals with all the possible changes to a caretaker
        elif choice == '3':
            caretakers = []
            how_many = int(input("How many caretakers would you like to add?:\n" + PROMPT))
            for x in range(how_many):
                a = input("Please enter the employee's id:\n" + PROMPT)
                b = input("Please enter the zoo subsection to work in:\n" + PROMPT)
                c = input("Please enter the caretaker's specialty:\n" + PROMPT)
                caretakers.append([a,b,c])
            sql_funcs.add_caretaker(DB_FILE, caretakers)
        
        # Branching that deals with all the possible changes to an employee based on ID
        elif choice == '4':
            update_choice = "TBD"
            continue_choice = 'yes'
            employee_options = {
                '1': "The employee's first name.",
                '2': "The employee's middle initial.",
                '3': "The employee's last name.",
                '4': "The employee's phone number.",
                '5': "The employee's starting date.",
                '6': "The employee's sex.",
                '7': "The employee's age.",
                '8': "The employee's salary.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            eid = input("Please enter the employee's id:\n" + PROMPT)
            while(update_choice.lower() == 'yes'):
                print("What information about the employee would you like to update?")
                for option, desc in employee_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                
                update_choice = input(PROMPT)
            
                fname,minit,lname,pn,s_date,sex,age,salary = 0,0,0,0,0,0,0,0
                
                # Branching to account for specific changes 
                if update_choice == '1':
                    fname = input("Please enter a new first name:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '2':
                    minit = input("Please enter a new middle initial:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '3':
                    lname = input("Please enter a new last name:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '4':
                    pn = input("Please enter a new phone number:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '5':
                    s_date = input("Please enter a new starting date:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '6':
                    sex = input("Please enter a new sex:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '7':
                    age = input("Please enter a new age:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == '8':
                    salary = input("Please enter a new salary:\n" + PROMPT)
                    sql_funcs.update_employee(DB_FILE,eid,fname,minit,lname,pn,s_date,sex,age,salary)
                elif update_choice == 'b' or update_choice == 'back':
                    continue
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the employee?(yes or no)\n" + PROMPT)

        # Deals with changes to manager
        elif choice == '5':
            update_choice = "TBD"
            continue_choice = 'yes'
            manager_options = {
                '1': "The managers's zoo subsection.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            eid = input("Please enter the manager's id:\n" + PROMPT)
            while(update_choice.lower() == 'yes'):
                print("What information about the manager would you like to update?\n" + PROMPT)
                for option, desc in manager_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                update_choice = input(PROMPT)

                # Branching to deal with changes in manager
                if update_choice == '1':
                    zoo_sub = input("Please enter the new zoo subsection:\n" + PROMPT)
                    sql_funcs.update_manager(DB_FILE,eid,zoo_sub)
                elif update_choice == 'b' or update_choice == 'back':
                    menu_manager()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the manager?(yes or no)\n" + PROMPT)

        # Deals with changes to caretaker 
        elif choice == '6':
            update_choice = "TBD"
            continue_choice = 'yes'
            caretaker_options = {
                '1': "The caretaker's zoo subsection.",
                '2': "The caretaker's specialty.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            # Prints menu
            eid = input("Please enter the caretaker's id:\n" + PROMPT)
            while(update_choice.lower() == 'yes'):
                print("What information about the caretaker would you like to update?\n" + PROMPT)
                for option, desc in caretaker_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                update_choice = input(PROMPT)

                zoo_sub, specialty = 0,0

                # Branching that deals with user changes to caretaker
                if update_choice == '1':
                    zoo_sub = input("Please enter a new zoo subsection:\n" + PROMPT)
                    sql_funcs.update_caretaker(DB_FILE,eid,zoo_sub,specialty)
                elif update_choice == '1':
                    specialty = input("Please enter a new specialty:\n" + PROMPT)
                    sql_funcs.update_caretaker(DB_FILE,eid,zoo_sub,specialty)
                elif update_choice == 'b' or update_choice == 'back':
                    menu_manager()
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the caretaker?(yes or no)\n" + PROMPT)
        # Deletes employee
        elif choice == '7':
            eid = input("Please enter the employee's id to be deleted:\n" + PROMPT)
            sql_funcs.delete_employee(DB_FILE, eid)
        # Deletes manager based on ID input
        elif choice == '8':
            eid = input("Please enter the manager's id to be deleted:\n" + PROMPT)
            sql_funcs.delete_manager(DB_FILE, eid)
        # Deletes caretaker based on ID input
        elif choice == '9':
            eid = input("Please enter the caretaker's id to be deleted:\n" + PROMPT)
            sql_funcs.delete_caretaker(DB_FILE, eid)
        elif choice == '10':
            sql_funcs.all_employees(DB_FILE)
            waitKey()
        # Goes back 
        elif choice == 'b' or choice == 'back':
            return
        # Exits
        elif choice == 'q' or choice == 'quit':
            exit()

def menu_edit_relationship():
    tko = input("Would you like to add or delete a relationship? (1 or 2):\n" + PROMPT)
    if tko == '1': # Option to add a takes_care_of relationship.
        ids = []
        how_many = int(input("Please enter how many relationships will be made:\n" + PROMPT))
        for x in range(how_many):
            eid = input("Please enter the caretaker's id:\n" + PROMPT)
            aid = input("Please enter the animal's id:\n" + PROMPT)
            ids.append([eid,aid])
        sql_funcs.add_takes_care_of(DB_FILE, ids)
    elif tko == '2': # Option to delete a takes_care_of relationship.
        eid = input("Please enter the caretaker's id:\n" + PROMPT)
        aid = input("Please enter the animal's id:\n" + PROMPT)
        sql_funcs.delete_takes_care_of(DB_FILE, eid, aid)

# Stats Menu
def menu_aggregrate_functions():
    choice = "TBD"
    options = {
        '1': "Average employee age.",
        '2': "Oldest age of employees.",
        '3': "Youngest age of employees.",
        '4': "Total count of animals in zoo.",
        'b': "Go back.",
        'back': "",
        'q': "Log out.",
        'quit': "",
    }
    # Displays menu
    while(choice not in ['b', 'back', 'q','quit']):
        clear_term()
        print("What would you like to do?")
        for option, desc in options.items():
            if option == 'b':
                print('(b)ack' + ". " + desc)
                continue
            if option == 'q':
                print('(q)uit' + ". " + desc)
                continue
            if option in ['back', 'quit']:
                continue
            print(option + ". " + desc)
        
        choice = input(PROMPT)
        
        if choice == '1': # Average age function
            sql_funcs.avg_employee_age(DB_FILE)
            waitKey()
        elif choice == '2': # Max age function
            sql_funcs.max_employee_age(DB_FILE)
            waitKey()
        elif choice == '3': # Min age function
            sql_funcs.min_employee_age(DB_FILE)
            waitKey()
        elif choice == '4': # Total animals in database
            sql_funcs.total_animal_count(DB_FILE)
            waitKey()

if __name__ == "__main__":
    zoo = ZooDatabase()
    zoo.load_users(USERS_FILE, ADMINS_FILE)
    user_choice = "TBD"

    print("Welcome " + zoo.current_user + " to your Zoo Access Terminal.")
    while(user_choice != "quit" and user_choice != "q"):
        user_choice = menu_login(zoo)



