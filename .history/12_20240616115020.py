#2D LISTS
# 2D lists are lists that contain other lists. For example, the following list contains three lists of length 3:

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# To access elements in a 2D list, you need two indices. For example, to access the number 6 in the above list, you can use the following code:
# list_name[1][2]

# The first index refers to the outer list, and the second index refers to the inner list. In this case, the number 6 is in the second list (index 1) and the third element (index 2) of that list.

# You can also use a for loop to iterate over a 2D list. For example, the following code prints all the elements in the above list:

list_name = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list_name[2][4])

for x in list_name:
    print(x)
    for y in x:
        print(y)

# In this code, the outer loop iterates over each list in the 2D list, and the inner loop iterates over each element in the inner list. This allows you to access and process each element in the 2D list.