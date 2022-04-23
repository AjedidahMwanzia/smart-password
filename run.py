#!/usr/bin/env python3.8
from user import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    

