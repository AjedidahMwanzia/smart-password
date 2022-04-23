#!/usr/bin/env python3.8
from click import password_option
from user import User, Credentials
import pyperclip

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
    gen_password = Credentials.generate_password()
    return gen_password

def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


# .................................Credentials......................................

def new_credentials(account_name,username,password):
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

def main():
    print('Hello Welcome to smart-password. \n Please enter the following short codes to proceed.\n ac -- new account creation \n li-- log in \n ex --exit')

    short_code =input ("Enter a short_code choice: ").lower().strip()
    if short_code == "ac":
        print("register as a new user")
        print('*' * 60)
        username = input("username: ")
        while True:
            print("Tp to type your own password \n Gp -- to generate automatic password")
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
 


    
