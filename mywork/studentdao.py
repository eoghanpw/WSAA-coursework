import mysql.connector
import config as cfg


class StudentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        self.host = cfg.mysql["host"]
        self.user = cfg.mysql["user"]
        self.password = cfg.mysql["password"]
        self.database = "wsaa2"

    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        self.cursor.close()
        self.connection.close()

    def create(self, values):
        cursor = self.get_cursor()
        sql = ("INSERT into student (name, age) values (%s, %s)")
        cursor.execute(sql, values)
        self.connection.commit()
        new_id = cursor.lastrowid
        self.close_all()
        return new_id

    def get_all(self):
        cursor = self.get_cursor()
        sql = ("SELECT * from student")
        cursor.execute(sql)
        result = cursor.fetchall()
        self.close_all()
        return result

    def get_by_id(self, id):
        cursor = self.get_cursor()
        sql = ("SELECT * from student where id = %s")
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        self.close_all()
        return result

    def update(self, values):
        cursor = self.get_cursor()
        sql = ("UPDATE student SET name = %s, age = %s WHERE id = %s")
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()

    def delete(self, id):
        cursor = self.get_cursor()
        sql = ("Delete from student WHERE id = %s")
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()


studentDAO = StudentDAO()
