#SIMPLE REGISTER AND LOGIN SYSTEM EXERCISE

#We need to create a system in which a user can sign up and login to his account in terminal using everything you've learned so far!

class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def create_account(self):
        print("Account created successfully!")
    def login(self):
        print("Logged in successfully!")
    pass

print('Create your account')
try:
    username = input("Input your username: ")
    password = input("Input your password: ")


