#Program to understand how to write class,create object,create Constructor

""""
_init__ is a reseved method in python classes.
It is known as a constructor in object oriented concepts.
This method called when an object is created from the class
and it allow the class to initialize the attributes of a class.


self represents the instance of the class.
By using the “self” keyword we can access the attributes and methods
of the class in python
"""
class Student:
# instance attributes


    def __init__(self, name,age,address):
        self.name = name
        self.age = age
        self.address = address

    # instance methods (behaviours)
    def showinfo(self):
        return "Student Name is {} age is {} and Address {}".format(self.name,self.age,self.address)
""""
str.format() is one of the string formatting methods in Python3,
which allows multiple substitutions and value formatting.
This method lets us concatenate elements within a string through positional
formatting.
"""

# creating objects of class Student
ram=Student("Ram",24,"216,c Apartment,Solapur")
x=ram.showinfo()
print(x)
# accessing object information
print("age of {} is {}".format(ram.name, ram.age))