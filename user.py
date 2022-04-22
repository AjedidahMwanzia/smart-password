class User:
    """
    Class that generates new instances of user-details
    """
user_details = []
'''
__init__ method that helps us define properties for our objects.
'''
def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name =last_name
        self.phone_number =phone_number
        self.email= email

