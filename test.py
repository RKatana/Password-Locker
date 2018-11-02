import unittest
from account import User
from credentials import Credentials

class TestUser(unittest.TestCase):
  def setUp(self):
    self.new_user= User('Raphael','Katana','0720132613') #new user
    
    self.new_credentials= Credentials('1123','hjk') #new credentials

  def test_init(self):
    self.assertEqual(self.new_user.f_name,'Raphael')
    self.assertEqual(self.new_user.l_name,'Katana')
    self.assertEqual(self.new_user.p_number,'0720132613')

    #assert test for  credentials

    self.assertEqual(self.new_credentials.acc_name,'1123')
    self.assertEqual(self.new_credentials.password,'hjk')

  def tearDown(self):
    user_details=[]
    user_info=[]

  #test to check if user detailsare saved
  def test_save_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.user_info),2)

  #test to check if credentials are saved
    self.new_credentials.save_info()
    self.assertEqual(len(Credentials.user_details),2)

  #Test to check if multiple accounts can be saved
  def test_multi_save(self):
    self.new_user.save_user()
    self.new_user=User('Kk','pk','1432')
    self.assertEqual(len(User.user_info),1)

    #test for credentials
    self.new_credentials.save_info()
    self.new_credentials=Credentials('23','kde')
    self.assertEqual(len(Credentials.user_details),1)

  #test to check for profile and details
  def check_profile_name(self):
    new_user.save_user()
    









if __name__=='__main__':
  unittest.main()