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
