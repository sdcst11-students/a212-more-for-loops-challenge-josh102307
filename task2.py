#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

for i in range(1,4):
    username = input("enter your username: ")
    password = input("enter your password: ")
    if username == expectedUsername and password == expectedPassword:
        print("access granted")
        break
    if username != expectedUsername or password != expectedPassword:
        print("incorrect try again")
        

else:
    print("access denied")
