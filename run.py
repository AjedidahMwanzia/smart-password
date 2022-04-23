#!/usr/bin/env python3.8
from user import User, Credentials

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

def del_user(user):
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
    generate_password = Credentials.generate_password()
    return generate_password

# .................................Credentials......................................

def new_credentials(account_name,username,password):
    '''
	Function to create a new credential
	'''
    new_credentials = Credentials(account_name,username,password)
    return new_credentials
    