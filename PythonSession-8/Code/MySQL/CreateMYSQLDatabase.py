import mysql.connector #Import mysql.connector module

try:
	query="create Database Studentinfo"
	#Established Connection
	myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root")
	#Create Special Object of Cursor
	cur = myconn.cursor()
	cur.execute(query)#execute single query
	print("Database Created Successfully")
	

		

except mysql.connector.DatabaseError as err:
		if myconn!=None :
					myconn.rollback()
					print("\n Database Connection have issue : ",err)
			
finally :	
		cur.close()	
		print("\n Cursor Close")		
		myconn.close()	
		print("\n Connection Close")		
							

