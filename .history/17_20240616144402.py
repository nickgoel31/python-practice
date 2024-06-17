#CLASSES AND OBJECTS IN PYTHON (OOPS)

#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    name = "Grizzly the bear"
    age = 32
    #METHOD
    def animal_attribute(self):
        print("I am an animal")

#INHERITANCE
class Tiger(Animal):
    # CONSTRUCTOR
    def __init__(self):
        print("Created a Tiger rawr!")
    
tiger = Tiger()


#Explanation: In this program, we have created a class Animal as a base class and defined a method animal_attribute. We have created another class Tiger which is inheriting Animal and accessing the base class method. We have created an object of Tiger class and called the base class method using the object of the derived class. The output will be This is a base class method.
