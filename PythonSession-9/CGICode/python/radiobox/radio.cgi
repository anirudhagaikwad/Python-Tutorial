#!C:/Users/Vaishnavi/AppData/Local/Programs/Python/Python37/python.exe

import cgi
import cgitb # Import modules for CGI handling 
cgitb.enable()

# Create instance of FieldStorage
input_data=cgi.FieldStorage()

print('Content-Type:text/html') #HTML is following
print() 

# Get data from fields
# Get data from fields
if input_data.getvalue('item'):
						item = input_data.getvalue('item')
else:
   item = "Not set"


print("<h2> RadioBox Item is : %s</h2>" % item)
#print("<h2> RadioBox Cofee is : %s</h2>" % item2)

