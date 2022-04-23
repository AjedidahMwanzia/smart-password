import unittest 
from user import User, Credentials 


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
# .............................credential class.................................................................


class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials("Facebook","jeddy","12345")
    def  test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"Facebook")
        self.assertEqual(self.new_credentials.username,"jeddy")
        self.assertEqual(self.new_credentials.password,"12345")

    def test_save_credentials(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user_details
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        """
        self.new_credentials.save_credentials()
        test_credentials= Credentials("instagram","@ajedidah_","31526673")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credentials(self):

        """
        test_delete_user to test if we can remove a user from our user_list
        """
        self.new_credentials.save_credentials()
        test_credentials= Credentials("instagram","@ajedidah_","31526673")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()

    def test_display_credentials(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_find_credentials_by_account_name(self):

        '''
        test to check if we can return a Boolean  if we cannot find the credentialsusing account name.
        '''
        self.new_credentials.save_credentials()
        test_Credentials = Credentials("linkedin","AjedidahMwanzia","5811")
        test_Credentials.save_credentials()

        found_credentials = Credentials.find_by_account_name("linkedin")

        self.assertEqual(found_credentials.account_name,test_Credentials.account_name)

    
    def test_display_all_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


    

  
    
if __name__ == '__main__':
    unittest.main()