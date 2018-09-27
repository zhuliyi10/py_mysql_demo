import pymysql
class pymysql_operate(object):
    db_name = "test2_db"
    table_name="user"
    def connect_mysql(self):
        self.mydb = pymysql.connect(
            "localhost",
            "root",
            "123456",
            self.db_name
        )

    def create_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "CREATE TABLE if not exists {}(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT)".format(self.table_name)
        mycursor.execute(sql)
        mycursor.close()

    def drop_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "drop table if exists {}".format(self.table_name)
        mycursor.execute(sql)
        mycursor.close()

    def insert_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO {} (name,age) VALUES (%s,%s)".format(self.table_name)
        val = ("zhuly", 26)
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.lastrowid, "记录插入成功！")

    def update_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "update {} set name=%s where name=%s".format(self.table_name)
        val = ("zhuliyi", "zhuly")
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

    def del_date(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "delete from {} where id=5".format(self.table_name)
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录删除成功")

    def query_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        # sql = "select * from user where name='zhuly' order by age desc limit 2"
        sql = "select * from {}".format(self.table_name)
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for item in result:
            print(item)