
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_related(url: str) -> int:
    '''
    Given formatted url,
    the function returns a list of related titles..

    Note: need to check http request code to verify it is 200(OK)
    '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    
    book_list = soup.find('ul', class_="booklist").find_all('li')
    title_list = []
    for book in book_list:
        title = book.find('li', class_="recommendation-logged-out")
        print(title)
        if title != None:
            title_list.append(title.get_text())
    
    print(title_list)

    #print(book_list[:4])
    #firstBook = soup.find('a', attrs={'accesskey':'3'});
    #firstBookHref = firstBook['href']
    # firstBookHref is a string '/ebooks/XXXX'
    # remove '/ebooks/' part
    #bookID = firstBookHref[8:]
    #bookID = int(bookID)
    #return bookID


if __name__ == '__main__':

    path = "https://whatshouldireadnext.com/isbn/9781904633013"

    print(get_related(path))
