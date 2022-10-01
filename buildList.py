from isbnlib import meta
from isbnlib.registry import bibformatters

SERVICE = "openl"

# now you can use the service
isbn = "9780764548338"
bibtex = bibformatters["bibtex"]
print(bibtex(meta(isbn, SERVICE)))