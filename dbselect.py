import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="guvidb"
    )
mycursor=mydb.cursor()
mycursor.execute("select * from demo")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
