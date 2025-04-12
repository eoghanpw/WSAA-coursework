import mysql.connector
import config as cfg

db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database="wsaa2"
)

cursor = db.cursor()
sql = (
    "INSERT INTO student (name, age) values (%s, %s)"
)
values = ("Mary", 21)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
cursor.close()
db.close()
