#WORKING WITH FILES IN PYTHON

#Reading from a file
file = open('files/test.txt', "r")
print(file.read())
file.close()

#Writing a file
file2 = open('files/test2.txt', "w")
file2.write("Hello, World!")
file.close()

