import unittest 
from user import User 

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ajedidah","123456")
    def  test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"ajedidah")
        self.assertEqual(self.new_user.password,"123456")

# def test_save_user(self):
#     '''
#     test_save_user test case to test if the user object is saved into
#          the user_details
#     '''
#     self.new_user.save_user()
#     self.assertEqual(len(User.user_details),1)
    
if __name__ == '__main__':
    unittest.main()