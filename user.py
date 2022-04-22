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
        User.user_list.append(self) 


