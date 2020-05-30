import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="guvidb"
    )
mycursor=mydb.cursor()
sql=("insert into demo(name,id)values(%s,%s)")
val=("rishi",102)
mycursor.execute(sql,val)
mydb.commit()
