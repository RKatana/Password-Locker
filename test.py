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




if __name__=='__main__':
  unittest.main()