
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_recs(url):
    '''
    Get list of recommended titles from Goodreads, given url.
    '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    book_list = soup.find('table', class_="tableList")
    if book_list is None: return

    book_list = book_list.find_all('tr')
    title_list = []
    for book in book_list:
        title = book.find('span')
        #print(title)
        if title != None:
            title_list.append(title.get_text())

    return title_list


if __name__ == '__main__':
    url = "https://www.goodreads.com/book/similar/2422333"

    rec_list = get_recs(url)

    print(rec_list)
