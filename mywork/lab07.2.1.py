import mysql.connector
import config as cfg

connection = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
)

mycursor = connection.cursor()

mycursor.execute("CREATE database wsaa2")
mycursor.close()
connection.close()
