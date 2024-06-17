#FUNCTIONS IN PYTHON

#Functions are used to perform a specific task
#Functions are defined using the def keyword
def my_function():
    print("Hello from a function")


#Functions can take parameters
def my_function_with_args(username):
    print("Hello, " + username)

#Functions can return values
def sum(a,b):
    return a+b

#Multiple arguments but dont know the length of?
def sumWithNoLimit(*args):
    sum = 0
    for a in args:
        sum += a
    return sum


#Functions are called by their name
my_function()
my_function_with_args("John")
print(sum(1,2))

print(sumWithNoLimit(1,3,23,4,46,45))