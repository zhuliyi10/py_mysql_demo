import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
# sql = "select * from user where name='zhuly' order by age desc limit 2"
sql = "select * from user"
mycursor.execute(sql)
result = mycursor.fetchall()

for item in result:
    print(item)
