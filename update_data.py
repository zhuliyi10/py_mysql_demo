import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
sql = "update user set name=%s where name=%s"
val=("zhuliyi","zhuly")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")