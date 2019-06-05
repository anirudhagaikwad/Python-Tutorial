#Inheritance Example

#Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
"""
"__init__" is a reseved method in python classes.
It is known as a constructor in object oriented concepts.
This method called when an object is created from the class
and it allow the class to initialize the attributes of a class.
"""
		def __init__(self, name, age):
                    self.name = name
                    self.age = age
"""
self represents the instance of the class.
By using the “self” keyword we can access the attributes and methods
of the class in python
"""
    # instance method
        def description(self):
        return "{} is {} years old".format(self.name, self.age)
"""
str.format() is one of the string formatting methods in Python3,
which allows multiple substitutions and value formatting.
This method lets us concatenate elements within a string through positional
formatting.
"""
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class GermanShepherd(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
