import mysql.connector


class mysql_operate(object):
    db_name = "test2_db"

    def connect_mysql(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database=self.db_name
        )

    def create_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456"
        )
        mycursor = mydb.cursor()
        sql = "CREATE DATABASE {}".format(self.db_name)
        mycursor.execute(sql)

    def create_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "CREATE TABLE user(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT)"
        mycursor.execute(sql)

    def drop_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "drop table if exists user"
        mycursor.execute(sql)

    def insert_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO user (name,age) VALUES (%s,%s)"
        val = ("zhuly", 26)
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.lastrowid, "记录插入成功！")

    def update_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "update user set name=%s where name=%s"
        val = ("zhuliyi", "zhuly")
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

    def del_date(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "delete from user where id=5"
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录删除成功")

    def query_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        # sql = "select * from user where name='zhuly' order by age desc limit 2"
        sql = "select * from user"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for item in result:
            print(item)
