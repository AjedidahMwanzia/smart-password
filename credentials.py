
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

