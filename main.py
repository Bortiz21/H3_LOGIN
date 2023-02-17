# Homework 3 : User Login
# Program BY : Brandon Ortiz
# File Name  : H3_Login.py
# Function   : This program will authenticate user access

# Create the dictionary for the user logins
# ---------USE A DICT INSIDE A DICT-----------
# noinspection SpellCheckingInspection
users = {1: {'name': 'Mikey', 'pass': 'pizzatime', 'role': 'standard'},
         2: {'name': 'Donny', 'pass': 'halfshell', 'role': 'standard'},
         3: {'name': 'Ralph', 'pass': 'shredhead', 'role': 'standard'},
         4: {'name': 'Leo', 'pass': 'cowabunga', 'role': 'admin'}
         }

for user in users:
    print(users[user]['name'])
# The user should be asked if they already have an account, or if they'd like to create a new one.
verify = input(str("Are you an existing user? Y/N :"))

if verify.lower() == 'y':
    # If the user already has an account, they will be prompted to input their username and password

    user_name = input("Please enter in your User Name : ")
    user_pass = input("Please enter in your Password : ")

    user_credentials = user_name + ' ' + user_pass
    # If the credentials are found in the dictionary, they will be granted access.
    for user in users:
        if users[user]['name'] == str(user_name):
            # Once logged, the user's role is determined. A welcome message should be displayed if they are a
            # standard user.
            print("You are a user, congrats!")
            break
            # A list of all user accounts should be displayed if the user is an Administrator.
    else:
        print("You are not a user!")
elif verify.lower() == 'n':
    # If the user does not have an account, they will be prompted to enter a new username and password.
    new_acc_username = input("To create a new account please enter in a username : ")
    new_acc_pass = input("Please enter in a password : ")

    new_user = new_acc_username + ' ' + new_acc_pass
    # This information will then be inserted and stored in the dictionary.
else:
    print("Error - Invalid Input!")

