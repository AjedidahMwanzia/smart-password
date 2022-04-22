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
        self.new_user = User("Ajedidah","123456")
    def  test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Ajedidah")
        self.assertEqual(self.new_user.password,"123456")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user_details
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple users
        """
        self.new_user.save_user()
        test_user=User("Test","1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
   
    def test_delete_user(self):

        """
            test_delete_user to test if we can remove a user from our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","1234")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(),User.user_list)


    
if __name__ == '__main__':
    unittest.main()