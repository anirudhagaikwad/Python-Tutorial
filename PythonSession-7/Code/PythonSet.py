#Program to illustrate Python Set

my_set = {1.0, "Hello", (11, 22, 33)}
s={1,'A',2}
""""
A set is created by placing all the items (elements) 
inside curly braces {},separated by comma
"""
print(my_set)
print(s)
#Sets are mutable. But since they are unordered, indexing have no meaning
# add an element
my_set.add(2)
print(my_set)

# add multiple elements
my_set.update([2,3,4])
print(my_set)

""""
We can add single element using the add() method 
and multiple elements using the update() method. 
The update() method can take tuples,
 lists, strings or other sets as its argument.
"""

my_set.discard(4)
print("\n Discard()",my_set)

my_set.remove(3)
print("\n Remove() ",my_set)

""""
particular item can be removed from set using methods, discard() and 
remove().The only difference between the two is that, while using discard
()if the item does not exist in the set, it remains unchanged. 
But remove() will raise an error in such condition.
"""

my_set.clear()
print(my_set)
