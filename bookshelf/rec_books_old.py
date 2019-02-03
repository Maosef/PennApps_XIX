
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_related(isbn: str) -> list:
    '''
    Given ISBN number,
    the function returns a list of related titles (if they exist).

    Note: need to check http request code to verify it is 200(OK)
    '''

    url = "https://whatshouldireadnext.com/isbn/" + isbn

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    
    book_list = soup.find('ul', class_="booklist")
    if book_list is None: return

    book_list = book_list.find_all('li')
    title_list = []
    for book in book_list:
        title = book.find('li', class_="recommendation-logged-out")
        #print(title)
        if title != None:
            title_list.append(title.get_text())
    
    return title_list

if __name__ == '__main__':
    
    isbn = "9781904633013"
    #path = "https://whatshouldireadnext.com/isbn/9781904633013"

    print(get_related(isbn))
