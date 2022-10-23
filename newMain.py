"""
================================================================================
 Program:           newMain.py
 Software Engineer: Jonas Sharron
 Date:              01-October-2022

 Purpose:   This program will process isbn's stored in a file and export them to 
            a MySQL database.  The program will also check for isbn's that are
            not represented in the search service and export them to list for
            evaluation by the user.  A manuel entry and editing method is also 
            provided for user interaction.

Related Files:      
            variable            file                purpose
            --------------------------------------------------------------------
            workbookName        inventory.xlsx      -data input file
            dataframeName       dataframe.xlsx      -dataframe created to remove
                                                     duplicate isbn's from data
                                                     input file
            dbIsbnxls           dbxls.xlsx          -dataframe created from MySQL 
                                                     to create dbIsbn list 

Lists:
            isbn_list[]         -list created from input file (workbookName), 
                                 duplicates removed
            
            bad_list and good_list are created from isbn_list
            --------------------------------------------------------------------
            bad_list[]          -list of isbn's not available in search service
            good_list[]         -list of isbn's available in search service

            
            dbIsbn_list[]       -list generated from records in MySQL database
            dup_list[]          -list of duplicate values found in both 
                                 dbIsbn_list and isbn_list (these values are 
                                 removed from the isbn_list) 

        * these lists are written to text files in the log directory 
================================================================================
"""

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
import os
from termcolor import colored, cprint 
from colorama import Fore, Back, Style 
from tabulate import tabulate
from win32printing import Printer
import fpdf
import colorama
from colorama import Fore, Back, Style
import getopt

# retrieve stored information
# ===========================
filename = "dump"
file = open(filename, 'rb')
new = pickle.load(file)
lines = loadtxt(new, dtype=str, comments="#", delimiter=",", unpack=False)
file.close()

USER        = str(lines[0])
XWORD       = str(lines[1])
HOST        = str(lines[2])
DATABASE    = str(lines[3])
DATAFILE    = str(lines[4])
FNAME       = str(sys.argv[1])


# define external files
# ======================
workbookName    = DATAFILE
dataframeName   = "dataframe.xlsx"
dbIsbnxls       = "dbxls.xlsx"

# initialize lists
# =================
bad_list        = []
good_list       = []
isbn_list       = []
dbIsbn_list     = []
dup_list        = []

# establish database connection
# =============================
try:
    SUSERNAME     = str(lines[0])
    SPASSWORD     = str(lines[1])
    SHOST         = str(lines[2])
    SDATABASE     = str(lines[3])

    CONNECTION = mysql.connector.connect(user=SUSERNAME, password=SPASSWORD,
    host=SHOST, database=SDATABASE)
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
# user functions
# ==============================================================================

def createLists():
    """
    ============================================================================
    Function:       createLists()
    Purpose:        filters input data into two lists (good_list and bad_list)
                    depending on the availability of data in the search service
                    (filtered by return data from ('Authors') field)
    Parameter(s):   -None- (processes data in external file)
    Return:         -None- (propagates data in good_list and bad_list)
    ============================================================================
    """
    # iterate through data file and for existence in search service
    print("Checking search service for data file information")
    for i in isbn_list:
        isbn = i

        SERVICE = "openl"
        bibtex = bibformatters["bibtex"]
        
        # if data is not available in search service, add isbn to bad_list
        # otherwise add isbn to good_list
        # ==================================================================
        meta_dict = meta(isbn, service='default')
        if meta_dict.get('Authors') is None:
            bad_list.append(isbn)
        else:
            good_list.append(isbn)  

    # data file check completion message
    print("Check for datafile information completed, data with available "
        "information exported to good_list, data without information exported"
        " to bad_list")

def getInfo():    
    """
    ============================================================================
    Function:       getInfo()
    Purpose:        retrieves information (author, title, isbn, year, publisher)
                    from search service and propagates MySQL database with hew
                    record.
    Parameter(s):   -None- (processes data in good_list)
    Return:         -None- (exports data to MySQL database)
    ============================================================================
    """
    # pick search service
    flag = True
    while flag == True:
        print("")
        print("Please select search service: ")
        print("1\tGoogle Books")
        print("2\tWikipedia")
        print("3\tOpenLibrary")
        print("")
        print("Press ENTER to select default (OpenLibrary)")
        option = input("selection: ") or '3'

        if option == '1':
            SERVICE = "goob"
            flag = False
        elif option == '2':
            SERVICE = "wiki"
            flag = False
        elif option == '3':
            SERVICE ="openl"
            flag = False
        else:
            print("Please make a valid selection")
        print("")
    
    
    
    # iterate through good_list and retrieve data from search service
    print("Connecting to search service . . .")
    print("Retrieving information for good_list . . .")
    for i in good_list:

            isbn = i

            #SERVICE = "openl"

            bibtex = bibformatters["bibtex"]
            
            meta_dict = meta(isbn, service='default')

            aut = str(meta_dict['Authors'])
            aut = aut.replace("[","")
            aut = aut.replace("]","")
            author = aut.replace("'","")
            title = meta_dict['Title']
            isbn = meta_dict['ISBN-13']
            year = meta_dict['Year']
            publisher = meta_dict['Publisher']

            # define data to retrieve
            data = (isbn, year, publisher, author, title)

            # SQL query to insert data into to db
            mySql_insert_query = (
            "INSERT INTO isbn (isbn, year, publisher, author, title)"
            "VALUES (%s, %s, %s, %s, %s)"
            )
        
            cursor = CONNECTION.cursor()
            cursor.execute(mySql_insert_query, data)
            CONNECTION.commit()

    # completion message
    print("Available information added to SQL database")            
            

# ==============================================================================

def exportBad():
    """
    ============================================================================
    Function:       exportBad()
    Purpose:        exports bad list (isbn's not found in search service) to 
                    external file for evaluation
    Parameter(s):   -None- (processes data in bad_list)
    Return:         -None- (generates external file)    
    ============================================================================
    """
    with open(r'bad_list.txt', 'w') as fp:
        for i in bad_list:
            fp.write("%s\n" % i)
    
    fp.close()

def preProcess():
    """
    ============================================================================
    Function:       preProcess()
    Purpose:        looks for and removes duplicate isbn's from import file and 
                    pre-existing db 
    Parameter(s):   -None- (reads data from input file and db)
    Return:         -None- (writes data (duplicates removed) to isbn_list)
    ============================================================================
    """
    print("Checking for duplicates in source file . . .")


    # remove duplicates from isbn spreadsheet, save in dataframe spreadsheet
    data = pd.read_excel(workbookName, sheet_name = 'data', usecols = ['isbn'])
    data_first_record = data.drop_duplicates(keep="first")

    writer = pd.ExcelWriter(dataframeName, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    data_first_record.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add numeric cell formats.
    format1 = workbook.add_format({'num_format': '###0'})

    worksheet.set_column(1, 1, 18, format1)

    writer.save()

    dframe = openpyxl.load_workbook(dataframeName)
    sh = dframe.active

    # send dataframe data to isbn_list
    for row in sh.iter_rows(min_row=2, min_col=2, max_row=sh.max_row, max_col=2):
        for cell in row:
            isbn = str(cell.value)
            isbn_list.append(isbn)
    
    # create dbIsbn_list from database
    print("Checking for duplicates in database file . . .")
    query = "SELECT isbn FROM isbn"
    df = sql.read_sql('SELECT isbn FROM isbn', CONNECTION)
    df.to_excel(dbIsbnxls)

    dbexcel = openpyxl.load_workbook(dbIsbnxls)
    sh = dbexcel.active

    for row in sh.iter_rows(min_row=2, min_col=2, max_row=sh.max_row, max_col=2):
        for cell in row:
            isbn = str(cell.value)
            dbIsbn_list.append(isbn)
    
    # compare isbn_list and dbIsbn_list and create intersection (duplicates) list
    a = (isbn_list)
    b = (dbIsbn_list)


    intersection = set(a).intersection(b)
    

    # remove intersection (duplicates) list values from isbn_list
    for value in intersection:
        if value in isbn_list:
            dup_list.append(value)
            isbn_list.remove(value)

    # completion of duplicate check message
    print("Duplicate check completed, duplicates removed and exported to dup_list")

def getGenre():
    """
    ============================================================================
    Function:       getGenre()
    Purpose:        imports genre information into MySQL database from external 
                    file
    Parameter(s):   -None- (reads data from input file and db)
    Return:         -None- (writes genre data to MySQL)
    ============================================================================
    """    
       
    # create datafrane from external file
    gframe = openpyxl.load_workbook(workbookName)
    data = gframe.active
    
    # define max row with x and y variables
    x = data.max_row
    y = 'B' + str(x) 
    
    cells = data['A2' : y]

    # iterate through external file to retrieve genre values
    for c1, c2 in cells:
        gisbn = (c1.value)
        gisbn = str(gisbn)
        genre = (c2.value)
        genre = str(genre)

        sqldata = (genre, gisbn)

        # define MySQL query and import genre values into database
        genre_query = ("UPDATE isbn SET genre = (%s) WHERE isbn = (%s)")
        
        cursor = CONNECTION.cursor()
        cursor.execute(genre_query, sqldata)
        CONNECTION.commit()

def menu():
    """
    ============================================================================
    Function:       menu()
    Purpose:        entry point to allow user interaction with program
    Parameter(s):   -None-
    Return:         users desired action
    ============================================================================
    """
    os.system('cls')

    # format screen
    # --------------
    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print("isbn-22 v0.01".rjust(80))
    print("--------------------".rjust(80))
    print(Style.RESET_ALL)

    # main menu
    #----------
    goAgain = 1

    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'MAIN MENU')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\tSet System Parameters')
        print('2\tProgram Functions')
        print('3\tReports')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tEXIT')
        print(Style.RESET_ALL)
        print('')
        print('')    

        # menu options based on user input
        # ---------------------------------
        menuOption = input("selection: ")

        if menuOption == '1':
            sysParmMenu()
        elif menuOption == '2':
            programFunctMenu()
        elif menuOption == '3':
            reportsMenu() 
        elif menuOption == '0':    
            goAgain = 0 

        os.system('cls')   

def sysParmMenu():
    """
    ============================================================================
    Function:       sysParmMenu()
    Purpose:        provides user options for editing program parameters
    Parameter(s):   -None- 
    Return:         users desired action
    ============================================================================
    """
    goAgain = 1
 
    # global values for MySQL
    # -----------------------
    global USER 
    global XWORD
    global HOST
    global DATABASE
    global DATAFILE
    global FNAME
    
    # system parameters menu
    # ----------------------
    while goAgain == 1:
        os.system('cls')
        now = datetime.datetime.now()
        print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
        print("isbn-22 v0.01".rjust(80))
        print("--------------------".rjust(80))
        print(Style.RESET_ALL)
        print('')
        print(Fore.GREEN + 'SET SYSTEM PARAMETERS')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print(Fore.RED +"PLEASE NOTE: if the values filename, location, or values "
            "are edited, the program will have to be restarted for the changes to "
            "take effect")
        print(Style.RESET_ALL)
        print('')
        print('1\tDisplay Values File Filepath and Name')
        print('2\tDisplay and Edit Values File')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tRETURN')
        print(Style.RESET_ALL)
        print('')
        print('')    

        # menu options based on user input
        # ---------------------------------
        menuOption = input("selection: ")

        if menuOption == '1':                     
            print('')
            print(Fore.YELLOW + str(FNAME)) 
            print(Style.RESET_ALL)
            print('')
            wait = input("Press ENTER to return")
        elif menuOption == '2':
            goAgain2 = 1
            while goAgain2 == 1:
                os.system('cls')
                now = datetime.datetime.now()
                print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                print("isbn-22 v0.01".rjust(80))
                print("--------------------".rjust(80))
                print(Style.RESET_ALL)
                print('')
                print(Fore.GREEN + 'VALUES FILE')
                print(Fore.GREEN + '-------------------')
                print(Style.RESET_ALL)
                print(Fore.RED + "These values should be kept secure and not "
                     "shared")
                print(Style.RESET_ALL)
                print('')
                # submenu for MySQL options
                # -------------------------
                print('1\tSet MySQL username')
                print('2\tDisplay MySQL username')
                print('3\tMySQL password')
                print('4\tDisplay MySQL password')
                print('5\tSet MySQL host address')
                print('6\tDisplay MySQL host address')
                print('7\tSet MySQL database name')
                print('8\tDisplay MySQL database name')
                print('9\tSet data file name and location')
                print('10\tDisplay data file name and location')
                print('')
                print('')
                print('')
                print(Fore.RED + '0\tRETURN')
                print(Style.RESET_ALL)
                print('')
                print('')    

                # menu options based on user input
                # ---------------------------------
                submenuOption = input("selection: ")
                if submenuOption == '1':
                    os.system('cls')
                    now = datetime.datetime.now()
                    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                    print("isbn-22 v0.01".rjust(80))
                    print("--------------------".rjust(80))
                    print(Style.RESET_ALL)
                    USER = input("Please Enter your MySQL username: ")
                if submenuOption == '2':
                    print('')
                    print(Fore.YELLOW + USER) 
                    print(Style.RESET_ALL)
                    print('')
                    wait = input("Press ENTER to return")
                if submenuOption == '3':
                    os.system('cls')
                    now = datetime.datetime.now()
                    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                    print("isbn-22 v0.01".rjust(80))
                    print("--------------------".rjust(80))
                    print(Style.RESET_ALL)
                    XWORD = input("Please Enter your MySQL password: ")
                if submenuOption == '4':
                    print('')
                    print(Fore.YELLOW + XWORD) 
                    print(Style.RESET_ALL)
                    print('')
                    wait = input("Press ENTER to return")
                if submenuOption == '5':
                    os.system('cls')
                    now = datetime.datetime.now()
                    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                    print("isbn-22 v0.01".rjust(80))
                    print("--------------------".rjust(80))
                    print(Style.RESET_ALL)
                    HOST = input("Please Enter your MySQL host address: ")
                if submenuOption == '6':
                    print('')
                    print(Fore.YELLOW + HOST) 
                    print(Style.RESET_ALL)
                    print('')
                    wait = input("Press ENTER to return")
                if submenuOption == '7':
                    os.system('cls')
                    now = datetime.datetime.now()
                    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                    print("isbn-22 v0.01".rjust(80))
                    print("--------------------".rjust(80))
                    print(Style.RESET_ALL)
                    DATABASE = input("Please Enter your MySQL database name: ")
                if submenuOption == '8':
                    print('')
                    print(Fore.YELLOW + DATABASE) 
                    print(Style.RESET_ALL)
                    print('')
                    wait = input("Press ENTER to return")
                if submenuOption == '9':
                    os.system('cls')
                    now = datetime.datetime.now()
                    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                    print("isbn-22 v0.01".rjust(80))
                    print("--------------------".rjust(80))
                    print(Style.RESET_ALL)
                    print(Fore.YELLOW + "Please use double backslashes (\\\) when "
                    "defining file path") 
                    print(Style.RESET_ALL)
                    DATAFILE=input("Please Enter your datafile name including path: ")
                if submenuOption == '10':
                    print('')
                    print(Fore.YELLOW + DATAFILE) 
                    print(Style.RESET_ALL)
                    print('')
                    wait = input("Press ENTER to return")
                elif submenuOption == '0':
                    goAgain2 = 0


        # elif statement to return to rewrite pickle file and return to previous
        # menu
        # ----------------------------------------------------------------------
        elif menuOption == '0':
            value = str(FNAME)
            vvfile = (USER+","+XWORD+","+HOST+","+DATABASE+","+DATAFILE)
            vfile = open(FNAME, "w")
            n = vfile.write(vvfile)
            vfile.close()
            filename = "dump"
            file = open(filename, 'wb')
            pickle.dump(value, file)
            file.close()
            goAgain = 0

        
    

def programFunctMenu():
    """
    ============================================================================
    Function:       programFunctMenu()
    Purpose:        provides user options for performing program functions
    Parameter(s):   -None- 
    Return:         users desired action
    ============================================================================
    """

    os.system('cls')

    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print("isbn-22 v0.01".rjust(80))
    print("--------------------".rjust(80))
    print(Style.RESET_ALL)

    goAgain = 1

    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'PROGRAM FUNCTIONS')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\tSearch for a Record')
        print('2\tEdit a Record')
        print('3\tManually Add a Record')
        print('')
        print('')
        print('4\tImport Records (with genre)')
        print('5\tImport Records (without genre)')
        print('')
        print('')
        print('5\tImport Genre')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tRETURN')
        print(Style.RESET_ALL)
        print('')
        print('')    

        menuOption = input("selection: ")

        if menuOption == '0':
            goAgain = 0 

def reportsMenu():
    """
    ============================================================================
    Function:       reportsMenu()
    Purpose:        provides user options for accessing reports
    Parameter(s):   -None- 
    Return:         users desired action
    ============================================================================
    """
    os.system('cls')

    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print("isbn-22 v0.01".rjust(80))
    print("--------------------".rjust(80))
    print(Style.RESET_ALL)

    goAgain = 1

    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'REPORTS')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\t')
        print('2\t')
        print('3\t')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tRETURN')
        print(Style.RESET_ALL)
        print('')
        print('')    

        menuOption = input("selection: ")

        if menuOption == '0':
            goAgain = 0   


# ==============================================================================
#  main entry point for program
#  =============================================================================    

def main():
    """
    ============================================================================
    Function:       main()
    Purpose:        entry point to program
    Parameter(s):   -None-
    Return:         -None-
    ============================================================================
    """
    global CONNECTION
    #preProcess()
    #createLists()
    #getInfo()
    #exportBad()
    #getGenre()
    menu()
    print("Closing Database Connection . . .")
    CONNECTION.close()
    print("bye . . .")

if __name__ == "__main__":
    main()

