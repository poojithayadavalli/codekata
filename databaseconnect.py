import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="guvidb"
    )
mycursor=mydb.cursor()
print("operations||\n1.insert\n2.update\n3.delete")
n=int(input())
n1=1
while n1>0:
    if n==1:
        name1=input("enter name")
        id1=input("enter id")
        sql=("insert into demo(name,id) values(%s,%s)")
        val=(name1,id1)
        mycursor.execute(sql,val)
        mydb.commit()
        n=int(input("continue? 1"))
    elif n==3:
        id2=int(input("enter the id to delete"))
        mycursor.execute("delete from demo where id=%s",id2)
        mydb.commit()
        n=int(input("continue? 1"))
    elif n==2:
        id3=input("enter id to be updated")
        name2=input("enter new name")
        sql="update demo set name=%s where id=%s"
        val=(name2,id3)
        mycursor.execute(sql,val)
        mydb.commit()
        n=int(input("continue? 1"))
    else:
        exit()


    
    
    


