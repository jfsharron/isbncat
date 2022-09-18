"""
================================================================================
 Program:
 Software Engineer:
 Date:

 Purpose:



compilation file to create full ISBN
================================================================================
"""

import sys
#from isbntools.app import *
import pandas
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("inventory.xlsx")
  
sh = wrkbk.active



# initialize lists
bad_list = []
good_list = []


# Input Variables
def createLists():
    """
    ============================================================================
    Function:
    Purpose:
    Parameter(s):
    Return:

    creates good_list and bad_list from imported .xlsx file
    ============================================================================
    """

    # iterate through excel and display data
    for row in sh.iter_rows(min_row=2, min_col=1, max_row=63, max_col=1):
        for cell in row:
            isbn = str(cell.value)

            SERVICE = "openl"

            bibtex = bibformatters["bibtex"]
            
            meta_dict = meta(isbn, service='default')

            if meta_dict.get('Authors') is None:
                bad_list.append(isbn)
            else:
                good_list.append(isbn)

    #print("bad list ", bad_list)
    #print("good list ", good_list)

    # ==========================================================================

def getInfo():    
    """
    ============================================================================
    Function:
    Purpose:
    Parameter(s):
    Return:

    ============================================================================
    """
    for i in good_list:
        #for cell in row:
            isbn = i

            SERVICE = "openl"

            bibtex = bibformatters["bibtex"]
            
            meta_dict = meta(isbn, service='default')

            author = str(meta_dict['Authors'])
            author = author.replace("[","")
            author = author.replace("]","")
            author = author.replace("'","")
            title = meta_dict['Title']
            isbn13 = meta_dict['ISBN-13']
            year = meta_dict['Year']
            publisher = meta_dict['Publisher']

            print ("Author(s):\t", author)
            print ("Title:\t\t", title)
            print ("ISBN:\t\t", isbn13)
            print ("Year:\t\t", year)
            print ("Publisher:\t", publisher)

# ==============================================================================

def exportBad():
    """
    ============================================================================
    Function:
    Purpose:
    Parameter(s):
    Return:

    
    ============================================================================
    """
    with open(r'bad_list.txt', 'w') as fp:
        for i in bad_list:
            fp.write("%s\n" % i)
    
    fp.close()


def main():
    """
    ============================================================================
    Function:
    Purpose:
    Parameter(s):
    Return:

    creates good_list and bad_list from imported .xlsx file
    ============================================================================
    """
    createLists()
    getInfo()
    exportBad()

if __name__ == "__main__":
    main()

