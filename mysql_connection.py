import mysql.connector
import os

def show_all():
    os.system("clear")


    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Zb01101944!?*",
        database="example"
    )

    cursor = connection.cursor()

    testQuery = 'SELECT * FROM student'

    cursor.execute(testQuery)

    for item in cursor:
        print(item)

    cursor.close()
    connection.close()

show_all()