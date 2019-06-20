#!C:/Users/Vaishnavi/AppData/Local/Programs/Python/Python37/python.exe

import cgi
import cgitb # Import modules for CGI handling 
cgitb.enable()

# Create instance of FieldStorage
input_data=cgi.FieldStorage()

print('Content-Type:text/html') #HTML is following
print() 

# Get data from fields
if input_data.getvalue('textcontent'):
							text_content = input_data.getvalue('textcontent')
else:
   text_content = "Not entered"


print("<h2> Text content is : %s</h2>" %text_content )
#print("<h2> RadioBox Cofee is : %s</h2>" % item2)

