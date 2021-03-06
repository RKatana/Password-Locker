import pyperclip
import random
from account import User 
class Credentials:
  '''
  class for user credentials
  '''
  user_details=[]

  random_pswd = ['acdbe4','ac5de','4ac4e','wat21','crde3']

  def __init__(self,acc_name,password):
    self.acc_name=acc_name
    self.password=password

  @classmethod
  def random_generator(cls):
    '''
    random pswd generator
    '''
    for pswd in cls.random_pswd:
      
      return pswd.random.choice(random_pswd)

  def save_info(self):
    '''
    save user credentials
    '''
    Credentials.user_details.append(self)

  def del_user(self):
    Credentials.user_details.remove(self)

  @classmethod
  def search_acc_name(cls,name):
    for account in cls.user_details:
      if account.acc_name == name:
        return account
      

  @classmethod
  def acc_exist(cls,name):
    for account in cls.user_details:
      if account.acc_name == name:
        return True
      return False


  @classmethod
  def show_details(cls):
    '''
    show user credentials
    '''
    return cls.user_details
