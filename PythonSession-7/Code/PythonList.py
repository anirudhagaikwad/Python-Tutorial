#Program to illustrate Python List

my_list = ['X',1,2,3,4,5,6,7,8,'W'] 
""""
list is created by placing all the items (elements) inside a square bracket [ ], 
separated by commas.
"""
print("\n List Elemets ['X',1,2,3,4,5,6,7,8,'W'] \n ")
print(my_list[0]) #We can use the index operator [] to access an item in a list. Index starts from 0.

print(my_list[-1])
print(my_list[-2])
""""
Python allows negative indexing for its sequences. 
The index of -1 refers to the last item,
-2 to the second last item and so on.
"""
print("\n elements 3rd to 5th ")
print(my_list[2:5]) # elements 3rd to 5th
print("\n elements beginning to 4th ")
print(my_list[:-5])# elements beginning to -4 
print("\n elements 6th to end ")
print(my_list[5:])# elements 6th to end
print("\n elements beginning to end  ")
print(my_list[:])# elements beginning to end


# change the 1st item    
my_list[0] = 8            

print(my_list)

# change 2nd to 4th items
my_list[1:4] = [3, 5, 7]  
print(my_list)

my_list.append(7) #add one item to a list using append() method
print(my_list)

my_list.extend([9, 11, 13])#add several items using extend() method.
print(my_list)

my_list.insert(1,3)#insert one item at a desired location by using the method insert()
print(my_list)

my_list[2:2] = ['A','B']
print(my_list)

del my_list[2]#delete one or more items from a list using the keyword del.
print(my_list)

del my_list[1:5]#Delete Mutiple Items
print(my_list)

my_list.remove(13)
print(my_list)#remove() method to remove the given item

my_list.pop(1)#pop() method to remove an item at the given index.
print(my_list)
""""
The pop() method removes and returns the last item if index is not provided. 
This helps us implement lists as stacks (first in, last out data structure).
"""
my_list.clear()#clear() method to empty a list.
print(my_list)




