
import random
import string
import pyperclip


class User:
    """
    Class that generates new instances of user-details
    """
    user_list = []

    def __init__(self, username, password):
        """
         method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_contact method saves user objects into user_list
        """
        User.user_list.append(self) 

    def delete_user(self):
        """
         delete_user method deletes a saved user from the user_list
        """
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
# ..................................credentials class.............................................................

class Credentials:
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    def __init__(self,account_name,username, password):
        """
        method that defines user credentials to be stored
        """
        self.account_name = account_name
        self.username = username
        self.password = password
    
    def save_credentials(self):
       """
       save_credentials method saves credentials objects into credentials_list
       """
       Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes credentials objects into credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list


    @classmethod
    def find_by_account_name(cls,account_name):
        """
        Method that takes in a account_name and returns credentials that matches that account_name.
        """
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list

    
    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))

    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)


  



