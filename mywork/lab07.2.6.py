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
    "DELETE from student "
    "WHERE id = %s"
)

values = (1,)

cursor.execute(sql, values)

print(f"Deleted ID: {values}")

cursor.close()
db.close()
