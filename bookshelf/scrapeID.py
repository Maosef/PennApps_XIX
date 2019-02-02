
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getFirstBookID(url: str) -> int:
    ''' 
    Given gutenberg url in the form 
    "http://www.gutenberg.org/ebooks/search/?query=pride+and+prejudice"
    the function returns the first book's ID as an integer.
    '''
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    firstBook = soup.find('a', attrs={'accesskey':'3'});
    firstBookHref = firstBook['href']
    # firstBookHref is a string '/ebooks/XXXX'
    # remove '/ebooks/' part
    bookID = firstBookHref[8:]
    bookID = int(bookID)
    return bookID



