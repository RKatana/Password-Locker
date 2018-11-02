import unittest
from account import User
from credentials import Credentials

class TestUser(unittest.TestCase):
  def setUp(self):
    self.new_user= User('Raphael','Katana','0720132613')

  def __init__(self):
    self.assertEqual(User.f_name,'Raphael')

if __name__=='__main__':
  unittest.main()