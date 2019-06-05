# Python Programm to understand how to write Numbers Data type
""""
type() function to know which class a variable or a value belongs to
and the isinstance()function to check if an object belongs to
a particular class."""
a = 5#Integer
print(a, "is of type", type(a))
a = 2.0#Float
print(a, "is of type", type(a))
a = 1+2j#Complex
print(a, "is complex number?", isinstance(1+2j,complex))
