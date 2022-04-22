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
    
