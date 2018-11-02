import pyperclip
import random
import User from account
class Credentials:
  '''
  class for user credentials
  '''
  user_details=[]

  random_pswd=['acdbe4','ac5de','4ac4e','wat21','crde3']

  def __init__(self,acc_name,password):
    self.acc_name=acc_name
    self.password=password

  def random_generator():
    '''
    random pswd generator
    ''''
    return random.choice(random_pswd)

  def save_info(self):
    '''
    save user credentials
    '''
    Credentials.user_details.append(self)

  @classmethod
  def show_profile(cls):
    '''
    show user credentials
    '''
    return cls.user_details
