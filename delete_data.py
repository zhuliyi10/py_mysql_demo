import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
sql = "delete from user where id=5"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除成功")