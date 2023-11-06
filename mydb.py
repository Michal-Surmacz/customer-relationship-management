import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='ZCamrus1234',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")
