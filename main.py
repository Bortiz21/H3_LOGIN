# Homework 3 : User Login
# Program BY : Brandon Ortiz
# File Name  : H3_Login.py
# Function   : This program will authenticate user access

users = {1: {'name': 'Mikey', 'pass': 'pizzatime', 'role': 'standard'},
         2: {'name': 'Donny', 'pass': 'halfshell', 'role': 'standard'},
         3: {'name': 'Ralph', 'pass': 'shredhead', 'role': 'standard'},
         4: {'name': 'Leo', 'pass': 'cowabunga', 'role': 'admin'}
         }

# The user should be asked if they already have an account, or if they'd like to create a new one.
verify = input(str("Are you an existing user? Y/N :"))

if verify.lower() == 'y':
    # If the user already has an account, they will be prompted to input their username and password
    user_name = input("Please enter in your User Name : ")
    user_pass = input("Please enter in your Password : ")

    user_credentials = user_name + ' ' + user_pass
    # If the credentials are found in the dictionary, they will be granted access.
    for user in users:
        if users[user]['name'] == str(user_name) and users[user]['pass'] == str(user_pass):
            # Once logged, the user's role is determined. A welcome message should be displayed if they are a
            # standard user.
            current_user = users[user]['name']
            current_user_pass = users[user]['pass']
            current_role = users[user]['role']

            print("\nACCESS GRANTED : Welcome back " + current_user + "!")
            # A list of all user accounts should be displayed if the user is an Administrator.
            if current_role == 'admin':
                print("Here is a list of all current users :")
                for i in users:
                    print(users[i])
            break
    else:
        print("Sorry your information was NOT found!")
        print("ACCESS DENIED!")
elif verify.lower() == 'n':
    # If the user does not have an account, they will be prompted to enter a new username and password.
    new_acc_username = input("Please enter in your desired user name: ")
    new_acc_pass = input("Please enter in your desired password: ")
    new_user = new_acc_username + ' ' + new_acc_pass
    print("Thank you, your information has been stored.")

    # This information will then be inserted and stored in the dictionary.
    print("\nACCESS GRANTED: Welcome! ")
    users.update({5: {'name': new_acc_username, 'pass': new_acc_pass, 'role': 'standard'}})
else:
    print("Error - Invalid Input!")
