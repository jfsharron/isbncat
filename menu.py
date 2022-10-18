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

    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print("isbn-22 v0.01".rjust(80))
    print("--------------------".rjust(80))
    print(Style.RESET_ALL)

    goAgain = 1

    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'MAIN MENU')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\tSystem Parameters')
        print('2\tProgram Functions')
        print('3\tReports')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tEXIT')
        print(Style.RESET_ALL)
        print('')
        print('')    

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
    os.system('cls')

    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print("isbn-22 v0.01".rjust(80))
    print("--------------------".rjust(80))
    print(Style.RESET_ALL)

    goAgain = 1

    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'SYSTEM PARAMETERS')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\tLinked File Names and Locations')
        print('2\tMySQL Parameters')
        print('3\tSearch Service')
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


    
    
    
def main():
    """
    ============================================================================
    Function:       main()
    Purpose:        entry point to program
    Parameter(s):   -None-
    Return:         -None-
    ============================================================================
    """
    menu()

if __name__ == "__main__":
    main()