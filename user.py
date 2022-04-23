
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
    



