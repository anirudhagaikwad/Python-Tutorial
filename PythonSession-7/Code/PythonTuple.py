#Program to illustrate Python Tuple

my_tuple = (1, 2, 3,'W','X')
""""
A tuple is created by placing all the items (elements) inside parentheses 
(),separated by commas.
"""
print(my_tuple)

print(my_tuple[0]) 
print(my_tuple[-1])
""""
We can use the index operator [] 
to access an item in a tuple where the index starts from 0.
"""
print(my_tuple[1:4])
print(my_tuple[:-1])
print(my_tuple[7:])
print(my_tuple[:])

print(my_tuple + (4, 5, 6))
#We can use + operator to combine two tuples. This is also called concatenation

print(my_tuple.count('W'))# Returns the number of items x 
print(my_tuple.index('X'))# Returns the index of the item 


