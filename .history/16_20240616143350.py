#WORKING WITH FILES IN PYTHON

#Reading from a file
file = open('files/test.txt', "r")
print(file.read())

#Writing a file
file = open('files/test.txt', "w")
file.write("Hello, World!")

