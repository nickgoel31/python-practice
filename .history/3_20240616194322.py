#USER INPUT

name = input('Input your name: ')
# age = input('Input your age: ')

# if name.capitalize().isalpha() & age.isnumeric():
#     print("Your name is "+name + "\nYou are "+age+" years old")
# else:
#     print("Invalid name or age")

#PYTHON INPUT EXERCISE (WORD REPLACER)

sentence = input("Initial Sentence: ")
word = input("Word to be replaced: ")
newWord = input("New Word: ")
replace = sentence.replace(word, newWord)

print("Replaced Sentence: "+replace)