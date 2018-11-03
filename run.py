#!/usr/bin/env python3.6
from account import User
from credentials  import Credentials

def create_user(fname,lname,phone):
  new_user=User(fname,lname,phone)
  return new_user

def create_creds(nacc,npassword):
  new_details = Credentials(nacc,npassword)
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
  return User.show_profile()

def user_del(user):
  user.del_user()

def main():
  print('Welcome to password locker, Please enter your name')
  user_name = input()

  print(f'Hello {user_name}')
  print('\n')

  while True:
    print('Please use this short codes: na - create new account, da - display your accounts, fa - find account, del - del an account, rp - generate random password, ex - to exit')

    short_code = input().lower()
    if short_code == 'na':
      print('New Account')
      print('*'*10)
      print('Enter first name ....')
      f_name = input()

      print('Enter last name ....')
      l_name = input()

      print('Enter phone number ....')
      p_number = input()

      print('Enter account name')
      acc_name = input()

      print('Enter your password')
      password = input()

      save_user(create_user(fname,lname,phone))
      save_credentials(create_creds(nacc,npassword))

      print('\n')
      print(f'New {acc_name} account created '):
      print('\n')

    elif short_code == 'da':
      if  display_details():
        print(f'Accounts for {fname} ')
        print('\n')
        for account in display_details():
          print(f' {account.acc_name} {account.fname} {account.lname}')

      else print('\n')
      print('Whoops! No account found')
      print('\n')

    elif short_code == 'fa':
      print('Enter the name of account to search')
      account_search = input()
      if find_user(account_search):
        print(f'{search_acc_name.acc_name}')

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

if __name__=='main':

  main()