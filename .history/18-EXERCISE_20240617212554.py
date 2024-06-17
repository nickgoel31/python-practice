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

usernames = ["harsh"]
try:
    username = input("Input your username: ")
    if(usernames.index(username)):
        print("Username already exists")
        exit()
    password = input("Input your password: ")
except ValueError:
    print("Invalid input")
    exit()
else:
    account = Account(username,password)
    account.create_account()
    usernames.append(account.username)

if(account):
    print('Login to your account')
    try:
        username2 = input("Input your username: ")
        password2 = input("Input your password: ")
        if username2 != account.username or password2 != account.password:
            print("Invalid username or password")
            exit()
    except ValueError:
        print("Invalid input")
        exit()
    else:
        account = Account(username,password)
        account.login()

