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
  return User.search_acc_name(name)
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



if __name__=='main':
  main()