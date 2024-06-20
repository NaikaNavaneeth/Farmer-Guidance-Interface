import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="MARKETERATESDATA")
print("data base connected")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE RATES_REAL(STATE VARCHAR(30),PADDY INT,MAIZE INT,GROUNDNUT INT,COTTON INT,SUNFLOWER INT,WHEAT INT)")
print("table created")
