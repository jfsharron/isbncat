import sys
#from isbntools.app import *
import pandas
from isbnlib import meta
from isbnlib.registry import bibformatters
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("inventory.xlsx")
  
sh = wrkbk.active

bad_list = []
good_list = []
  
# iterate through excel and display data
for row in sh.iter_rows(min_row=2, min_col=1, max_row=63, max_col=1):
    for cell in row:
        #print(cell.value, end=" ")
        isbn = str(cell.value)

        SERVICE = "openl"

        bibtex = bibformatters["bibtex"]
        #print(bibtex(meta(isbn, SERVICE)))
        
        meta_dict = meta(isbn, service='default')
        #print(meta_dict)

       
        #author = meta_dict.get(str(meta_dict['Authors'], None)
        #author = meta_dict.get(str(meta_dict['Authors'])
        
        #meta_dict.get('Authors')

        if meta_dict.get('Authors') is None:
            #print(f'{isbn} written by {author}')
            print(f"{isbn} author unknown")
            bad_list.append(isbn)
        else:
            #print(f"{isbn} author unknown")
            print(f'{isbn} written by Authors')
            good_list.append(isbn)
        
        #if 'error' in response:
        #    print("error")
        #else:
        #    print ("Author(s):\t", author)
        
        
        #author = author.replace("[","")
        #author = author.replace("]","")
        #author = author.replace("'","")
        #title = meta_dict['Title']
        #isbn13 = meta_dict['ISBN-13']
        #year = meta_dict['Year']
        #publisher = meta_dict['Publisher']

        #print ("Author(s):\t", author)
        #print ("Title:\t\t", title)
        #print ("ISBN:\t\t", isbn13)
        #print ("Year:\t\t", year)
        #print ("Publisher:\t", publisher)


        s="Hello$ Python3$"
        s1=s.replace("$","")

    

print("bad list ", bad_list)
print("good list", good_list)

