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
    "UPDATE student "
    "SET name = %s, age = %s "
    "WHERE id = %s"
)
values = ("Joe", 33, 1)

cursor.execute(sql, values)

db.commit()
print("Updated")
cursor.close()
db.close()
