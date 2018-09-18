import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db"
)

mycursor = mydb.cursor()
sql = "CREATE TABLE user(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT)"
mycursor.execute(sql)