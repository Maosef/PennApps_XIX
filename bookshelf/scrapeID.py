
from bs4 import BeautifulSoup
from urllib.request import urlopen

def format_url(title):

    '''
    formats a book title into a gutenberg http request
    '''
    words = title.split(" ")
    query = "+".join(words)
    print(query)

    return "http://www.gutenberg.org/ebooks/search/?query=" + query 

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

if __name__ == '__main__':
    title = "pride and prejudice"
    url = format_url(title)
    print(url)
    print(getFirstBookID(url))



