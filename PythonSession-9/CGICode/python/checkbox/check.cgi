#!C:/Users/Vaishnavi/AppData/Local/Programs/Python/Python37/python.exe

import cgi
import cgitb # Import modules for CGI handling 
cgitb.enable()

# Create instance of FieldStorage
input_data=cgi.FieldStorage()

print('Content-Type:text/html') #HTML is following
print() 

# Get data from fields
if input_data.getvalue('item1'):
						item1_flag = "ON"
else:
   item1_flag = "OFF"

if input_data.getvalue('item2'):
						item2_flag = "ON"
else:
   item2_flag = "OFF"


print("<h2> CheckBox Tea is : %s</h2>" % item1_flag)
print("<h2> CheckBox Cofee is : %s</h2>" % item2_flag)

