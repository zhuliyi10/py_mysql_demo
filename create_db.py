import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)

mycursor = mydb.cursor()
sql = "CREATE DATABASE test_db"
mycursor.execute(sql)
