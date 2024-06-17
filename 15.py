#TRY EXCEPT IN PYTHON

try:
    a = 5 / 1
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally:
    print("This is the finally block")