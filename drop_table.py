import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
sql = "drop table if exists user"
mycursor.execute(sql)