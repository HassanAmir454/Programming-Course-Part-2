import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@sql.01",
    database = "paractice"
)

cursor = conn.cursor()
cursor.execute ("UPDATE orders SET user_id = 1 WHERE id = 3; UPDATE orders SET user_id = 2 WHERE id = 4;")

for row in cursor.fetchall():
    print(row)

conn.close()