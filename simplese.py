import sys
#from isbntools.app import *
import pandas
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl

isbn = str(9798653385322)

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