#!C:/Users/Vaishnavi/AppData/Local/Programs/Python/Python37/python.exe

import cgi
import cgitb # Import modules for CGI handling 
cgitb.enable()

# Create instance of FieldStorage
input_data=cgi.FieldStorage()

print('Content-Type:text/html') #HTML is following
print() 
# Get data from fields
num1 = input_data.getvalue('num1')
num2  = input_data.getvalue('num2')


print(num1,num2)

