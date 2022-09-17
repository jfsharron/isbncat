import sys
#from isbntools.app import *
import pandas
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl

# load excel with its path
#wrkbk = openpyxl.load_workbook("inventory.xlsx")
#  
#sh = wrkbk.active
  
SERVICE = "openl"
bibtex = bibformatters["bibtex"]
#print(bibtex(meta(isbn, SERVICE)))

meta_dict = meta('9780471164838', service='default')
#print(meta_dict)
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
s="Hello$ Python3$"
s1=s.replace("$","")
print()

