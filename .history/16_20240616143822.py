#WORKING WITH FILES IN PYTHON

#Reading from a file
file1 = open('files/test.txt', "r")
print(file1.readable())
# print(file.readlines()[0])

for lines in file.readlines():
    print(lines)

file.close()

#Writing a file
file2 = open('files/test2.txt', "w")
file2.write("Hello, World!")
file2.close()

#Appending into a file
file3 = open('files/test2.txt', "a")
file3.write("\nThis is appended text")
file3.close()
