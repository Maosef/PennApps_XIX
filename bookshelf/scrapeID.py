
'''

Scrapes the book ID of a book from Gutenberg

'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    #Start here
    #URL here
    url = "http://www.gutenberg.org/ebooks/search/?query=pride+and+prejudice"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    firstBook = soup.find('a', attrs={'accesskey':'3'});
    firstBookHref = firstBook['href']
    # firstBookHref is a string '/ebooks/XXXX'
    # remove '/ebooks/' part
    bookID = firstBookHref[8:]
    bookID = int(bookID)
    print(bookID)



if __name__ == "__main__":
    main()
