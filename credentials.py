
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


    # @classmethod
    # def credentials_exists(cls,account_name):
    #     """
    #     Method that checks if a credentials exists from the credentials list.
    #     """
    #     for credentials in cls.credentials_list:
    #         if credentials.account_name == account_name:
    #             return True
    #         return False

