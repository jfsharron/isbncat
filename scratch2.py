import sys
import pandas as pd
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl
import mysql.connector
from mysql.connector import Error
import functools
import xlsxwriter
import pandas.io.sql as sql
import numpy as np
import pickle
from numpy import loadtxt
from prettytable import from_db_cursor
from prettytable import PrettyTable
import datetime
from datetime import date
import os
from termcolor import colored, cprint 
from colorama import Fore, Back, Style 
from tabulate import tabulate
#from win32printing import Printer
import fpdf
import colorama
from colorama import Fore, Back, Style
import getopt
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import webbrowser
import time
from pretty_html_table import build_table
from sqlalchemy import create_engine

# ==============================================================================

try:
    CONNECTION = mysql.connector.connect(user='jfsharron', password='marie151414',
    host='192.168.2.107', database='isbn22')
    if CONNECTION.is_connected():
        db_Info = CONNECTION.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        global cursor
        cursor = CONNECTION.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

# ==============================================================================    

# ==============================================================================

mysql_search_query = ("SELECT * FROM cQuery")
cursor = CONNECTION.cursor(buffered = True)
cursor.execute(mysql_search_query)    
mytable = from_db_cursor(cursor)
print(mytable)
print('') 

# ==============================================================================

mysql_search_query = ("SELECT cq_id FROM cQuery")
cursor = CONNECTION.cursor(buffered = True)
cursor.execute(mysql_search_query)    
mytable = from_db_cursor(cursor)
print(mytable)
print('') 

# ==============================================================================
# code to return last cq_id value +1

mysql_cqid_query = ("SELECT cq_id FROM cQuery ORDER BY cq_id DESC LIMIT 1")
cursor = CONNECTION.cursor(buffered = True)
cursor.execute(mysql_cqid_query)
result = cursor.fetchall()
for row in result:
    cqid = (row[0]) 
    cqid += 1
    print(cqid)    
