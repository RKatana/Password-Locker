import pyperclip
class User:
  '''
  Stores user data
  '''
  user_info=[]

  def __init__(self,f_name,l_name,p_number):
    self.f_name=f_name
    self.l_name=l_name
    self.p_number=p_number

  def save_user(self):
    '''
    save user info
    '''
    User.user_info.append(self)

  def del_user(self):
    '''
    delete user info
    '''
    User.user_info.remove(self)

  @classmethod
  def check_user(cls,number):
    for user in cls.user_info:
      if user.p_number==number:
        return user

  @classmethod
  def show_profile(cls):
    '''
    show user profile
    '''
    return cls.user_info

