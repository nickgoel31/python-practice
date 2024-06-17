#CREATE A BASIC CALCULATOR
#Create a basic calculator that asks for two numbers and then asks for the operation to be performed on them.
#The calculator should support addition, subtraction, multiplication, and division.
#The result should be displayed to the user.

#SOLUTION
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    if float(num2) != 0:
        result = float(num1) / float(num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter either +, -, * or /")

print("Result of the operation performed is: ", )