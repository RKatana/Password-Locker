import pyperclip
import User from account
class Credentials:
  '''
  class for user credentials
  '''
  user_details=[]

  def __init__(self,acc_name,password):
    self.acc_name=acc_name
    self.password=password

  def save_info(self):
    '''
    save user credentials
    '''
    Credentials.user_details.append(self)
