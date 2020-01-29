# handle = open('students.txt', 'a')
# handle.write('Hello Python Students')
# handle.close()

# handle=open('students.txt', 'r')
# print(handle.read())   '''used to display all the file information'''
# print(handle.readline()) '''only used to read a line only'''
# print(handle.readlines()) '''used to read all lines but displays all in listing method'''

'''2 ota function banaune, 1ta le login garne ani aarko le register garne'''

# def register():
#     print("Register account")
#
# def login():
#     print('login')
#
# message=input('Do you have an account, y/n: ')
#
# if message =='y':
#     login()
# else:
#     register()

import os.path

if not os.path.exists('register.txt'):
    file = open('register.txt', 'w')
    file.close()


def register():
    username = input('Enter username:')
    if username in open('register.txt').read():
        print("username already exists")
        exit()
    password = input('Enter password:')
    confirm_password = input('Enter confirm password: ')
    if password != confirm_password:
        print("password and confirm_password not match")
        exit()
    handle = open('register.txt', 'a')
    handle.write(username)
    handle.write(' ')
    handle.write(password)
    handle.write('\n')
    handle.close()
    print("successfully registered")
    exit()


def login():
    username = input('Enter username:')
    password = input('Enter password:')
    get_user_data = open('register.txt').readlines()
    users = []
    for user in get_user_data:
        users.append(user.split())

    total_users = len(users)
    increment = 0
    login_success = 0
    while increment < total_users:
        uname = users[increment][0]
        passwd = users[increment][1]
        if username == uname and password == passwd:
            login_success = 1

        increment += 1

    if login_success == 1:
        print(f'Welcome {username}')
    else:
        print("username & password not match")


message = input('Do you have an account, y/n: ')

if message=='y':
    login()
else:
    register()

# def register():
#     username = input('Enter Username: ')
#     if username in open('register.txt').read():
#         print('username already exist')
#         exit()
#     password = input("enter Password: ")
#     confirm_password = input("enter confirm Password: ")
#     if password != confirm_password:
#         print('password not match')
#         exit()
#     handle = open('register.txt', 'a')
#     handle.write(username)
#     handle.write(' ')
#     handle.write(password)
#     handle.write('\n')
#     handle.close()
#     print("successfully registered")
#     exit()
