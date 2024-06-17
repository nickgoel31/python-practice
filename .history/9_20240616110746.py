#DICTIONARIES IN PYTHON

#Dictionaries are used to store data values in key:value pairs

#A dictionary is a collection which is unordered, changeable and indexed

#In Python dictionaries are written with curly brackets, and they have keys and values

#Dictionary items are ordered, changeable, and does not allow duplicates

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created

#CREATING DICTIONARY
d1 = {"key":"value", "key2":"value2"}



#ACCESSING ITEMS
#You can access the items of a dictionary by referring to its key name, inside square brackets
print(d1["key"])

#You can also use the get() method to access the items of a dictionary
print(d1.get("key2"))

#CHANGE VALUES
d1["key"] = "new value"
print(d1)

d2 = {
    "name":"John",
    "age":30,
    "city":"New York"
}

d3 = {
    
}


