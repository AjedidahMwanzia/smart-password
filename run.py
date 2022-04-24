#!/usr/bin/env python3.8
from click import password_option
from user import User
from user import Credentials



def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
# ................................. User  ....................................

def login_user(username,password):
    """
    function that checks whether a user exist and then logs the user in.
    """
    check_user = Credentials.verify_user(username,password)
    return check_user

def generate_password():
    '''
	Function to generate a password automatically
	'''
    gen_password = Credentials.generatePassword()
    return gen_password

def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


# .................................Credentials......................................

def create_new_credentials(account_name,username,password):
    '''
	Function to create a new credential
	'''
    new_credentials = Credentials(account_name,username,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_credentials()

def delete_credentials(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def display_credentials():  
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

# ............................................main..............

def smartpassword():
    print('Hello Welcome to smart-password. \n Please enter the following short codes to proceed.\n ac -- new account creation \n li-- log in ')
    print('')

    short_code =input ("Enter a short_code choice: ").lower().strip()
    if short_code == "ac":
        print("register as a new user")
        print('-' * 60)
        username = input("username: ")
        while True:
            print("Tp -- to type your own password \n Gp -- to generate automatic password")
            password_option = input().lower().strip()
            if password_option == 'tp':
                password = input("Enter your password:\n ")
                break
            elif password_option == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password. Try again")
    
        save_user(create_user(username,password))
        print('')
        print(f'New Account Created for: {username} using password: {password}')
    elif short_code == "li":
        print("-"*50)
        print("Enter your username and password to log in: ")
        username= input("username: ")
        password =input ("password:")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Smart Password")  
            print('\n')
    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n Gp - Generate A randomn password \n dl - Delete credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new Credentials")
            print ("-"*30)
            print("Account name: ")
            account_name = input().lower()
            print("Your username")
            username= print("")
            while True:
                print(" Tp - To type your own pasword if you already have an account:\n Gp - To generate random Password")
                password_option = input().lower().strip()
                if password_option == "tp":
                    password = input("Enter your own password\n")
                    break
                elif password_option == "gp":
                   password = generate_password()
                   break
                else:
                   print("invalid password Try again")
                save_credentials(create_new_credentials(account_name,username,password))
                print('\n')
                print(f"Account Credential for: {account_name} - UserName: {username} - Password:{password} created succesfully")
                print('\n')
        elif short_code == "dc":
            if display_credentials():
                print("Here is your credentials list")
                print("-"*20)
            else:
                print("You have not saved any credentials yet")
        elif short_code == "fc":
            print('Enter the account_name you want to look for')
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account_name}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account_name} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == "Gp":
            password = generate_password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")
         
          
                



 
if __name__ == '__main__':
    smartpassword()

    
