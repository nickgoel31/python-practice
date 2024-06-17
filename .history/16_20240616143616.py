#WORKING WITH FILES IN PYTHON

#Reading from a file
file = open('files/test.txt', "r")
print(file.readable())
print(file.readline())
file.close()

#Writing a file
file2 = open('files/test2.txt', "w")
file2.write("Hello, World!")
file2.close()

#Appending into a file
file3 = open('files/test2.txt', "a")
file3.write("\nThis is appended text")
file3.close()
