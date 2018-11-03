
from account import User
from credentials  import Credentials

def create_user(f_name,l_name,p_number):
  new_user=User(f_name,l_name,p_number)
  return new_user

def create_creds(acc_name,password):
  new_details = Credentials(acc_name,password)
  return new_details

def save_user(user):
  user.save_user()

def save_credentials(info):
  info.save_info()

def find_user(name):
  return Credentials.search_acc_name(name)
def user_check(name):
  return User.check_user(name)

def display_details():
  return Credentials.show_details()
  return User.show_profile()

def user_del(user):
  user.del_user()

def main():
  print('Welcome to password locker, Please enter your username')
  user_name = input()

  print(f'Hello {user_name}')
  print('-'*20)
  print('Complete the next step to register')

  print('Enter first name ....')
  f_name = str(input())

  print('Enter last name ....')
  l_name = str(input())

  print('Enter phone number ....')
  p_number = int(input())
  save_user(create_user(f_name,l_name,p_number))
  

  print('\n')

  while True:
    print('*'*20)
    print('Please use these short codes: na - create new account, da - display your accounts, fa - find account, del - del an account, rp - generate random password, ex - to exit')
    print(f'User: .... {f_name} {l_name}')
    short_code = input().lower()
    if short_code == 'na':
      print('New Account')
      print('*'*10)

      print('Enter account name ....')
      acc_name = input()

      print('Enter your password ....')
      password = input()

      save_credentials(create_creds(acc_name,password))
      

      print('\n')
      print(f'New {acc_name} account created')
      print('\n')

    elif short_code == 'da':
      if display_details():
        print(f'Accounts for {f_name} {l_name} ')
        print('\n')
        for account in display_details():
          print(f' {account.acc_name}')

      else:
        print('\n')
        print('Whoops! No account found')
        print('\n')

    elif short_code == 'fa':
      print('Enter the name of account to search')
      account_search = input()
      if find_user(account_search):
        print(f'{find_user.acc_name}')

      else:
        print('Account not found')

    elif short_code == 'del':
      print('Enter account name to delete')
      acc_del = input()
      acc = find_user(acc_del)
      user_del(acc)

    elif short_code == 'ex':
      
        print('Thank you, bye')
        break
    
    else:
      print('Wrong operation. Try again')

if __name__=='__main__':

  main()