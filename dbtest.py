import sys
#from isbntools.app import *
import pandas
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl
import mysql.connector
from mysql.connector import Error
import pymysql


try:
    connection = mysql.connector.connect(user='jfsharron', password='marie151414',
    host='192.168.2.107', database='isbn22')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
#finally:
#    if connection.is_connected():
#        cursor.close()
#        connection.close()
#        print("MySQL connection is closed")

isbn = '3216549878888'
author = 'theauthor'
year = '9999'
publisher = 'thepublisher'
title = 'thetitle'

insert_stmt= (
"INSERT INTO isbn (isbn, year, publisher, author, title)"
"VALUES (%s, %s, %s, %s, %s)"
)
data = (isbn, year, publisher, author, title)
#cursor = connection.cursor()
cursor.execute(insert_stmt, data)
connection.commit()
print(cursor.rowcount, "Record successfully inserted into isbn")
cursor.close()






#connection = pymysql.connect(host='192.168.2.107',
#    user='jfsharron',
#    password='marie151414',
#    database='isbn22')
# 
#try:
#    cursor = connection.cursor()
#    cursor.execute("select database();")
#    db = cursor.fetchone()
#    print("You're connected to database: ", db)
#except pymysql.Error as e:
#    print("Error while connecting to MySQL", e)
#finally:
#    cursor.close()
#    connection.close()
#    print("MySQL connection is closed")