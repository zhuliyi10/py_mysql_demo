import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
sql = "INSERT INTO user (name,age) VALUES (%s,%s)"
val = ("zhuly", 26)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.lastrowid, "记录插入成功！")
