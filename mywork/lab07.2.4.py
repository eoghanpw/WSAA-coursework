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
    "SELECT * from student "
    "WHERE id = %s"
)
values = (2,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)
cursor.close()
db.close()
