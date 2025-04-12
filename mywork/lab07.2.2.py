import mysql.connector
import config as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database="wsaa2"
)

mycursor = mydb.cursor()
sql = (
    "CREATE TABLE student"
    "(id INT AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(250),"
    "age INT)"
)

mycursor.execute(sql)

mycursor.close()
mydb.close()
