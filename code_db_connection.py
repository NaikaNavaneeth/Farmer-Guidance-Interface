import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
print("data base connected")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE MARKETERATESDATA")
print("data base created")
