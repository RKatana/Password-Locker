#!/usr/bin/env python3.6
from account import User
from credentials  import Credentials

def create_user(fname,lname,phone):
  new_user=User(fname,lname,phone)
  return new_user

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
  print('Welcome to password locker')



if __name__=='main':
  main()