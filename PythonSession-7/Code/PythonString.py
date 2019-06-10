#Program to illumy_stringate Python my_stringing

my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

""""
access individual characters using indexing and a range of characters 
using slicing.Index starts from 0. 
"""
#first character
print('my_string[0] = ', my_string[0])

#last character
print('my_string[-1] = ', my_string[-1])

#slicing 2nd to 5th character
print('my_string[1:5] = ', my_string[1:5])

#slicing 6th to 2nd last character
print('my_string[5:-2] = ', my_string[5:-2])

""""
The + operator use for concatenates two my_stringing 
"""
str="\n SES Python Class"
x=my_string+str
print(my_string)
print(str)
print(x)
""""
The enumerate() function returns an enumerate object. 
It contains the index and value of all the items in the string as pairs.
"""
list_enumerate = list(enumerate(x))
print(list_enumerate)

print('len(str) = ', len(str))

s='SES'
print(s.lower())
#print('lower(str)='lower(str))

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)


