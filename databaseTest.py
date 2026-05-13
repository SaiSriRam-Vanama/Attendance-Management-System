import mysql.connector

try:
    conn = mysql.connector.connect(
        username='root',
        password='root',
        host='localhost',
        database='face_recognition',
        port=3307
    )
    cursor = conn.cursor()
    cursor.execute("show databases")
    data = cursor.fetchall()
    print("Connected! Databases:", data)
    conn.close()
except Exception as e:
    print("Connection failed:", e)
