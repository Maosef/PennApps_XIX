
'''
Given a book title, make a REST API call to the Google
Books API and get the ISBN-10 of the first search result
that has an ISBN-10. If no ISBN-10 is found,
-1 is returned.

Note: Need to check http response 200 OK

Parameters:
Book title is assumed to be space delimited.

Task:
Make a REST API call to Google Books
using the book title.

We will get back a JSON with an 
array of volues or book entries.
Not all of them have an associated
ISBN-10.

We assume the book is popular enough to
have multiple Google Book entries.
So we go through each entry and find
the first entry with an ISBN-10.

We continue iterating until an entry
with an ISBN is found or we reach the end of 
the available entries. If no ISBN-10 is found,
then -1 is returned.
'''

from urllib.request import urlopen
import json
from pprint import pprint

def get_isbn_10(title: str) -> int:
    # Hard code title for now.
    # Note: var shadowing
    title = 'Pride and Prejudice'

    titleSplit = title.split(' ')
    formattedTitle = ''
    for i in range(len(titleSplit)):
        formattedTitle = formattedTitle + titleSplit[i]
        if i < (len(titleSplit) - 1):
            formattedTitle = formattedTitle + '+'
    # Now, formattedTitle is same as title, but
    # delimited with + instead of spaces
    baseURL = r'https://www.googleapis.com/books/v1/volumes?q='
    apiKey = 'AIzaSyCIuNkPSTasaBxa2Bx2qivCLWwwlZC1B70'
    apiURL = baseURL + formattedTitle + '&key=' + apiKey
    
    request = urlopen(apiURL)
    contents = request.read()
    # type of contents should be bytes
    # now parse from JSON into python dict
    parsed = json.loads(contents)

    # Find ISBN, should be under
    # industryIdentifiers
    list_of_entries = parsed['items']
    isbn10 = -1
    for entry in list_of_entries:
        identifiers_list = entry['volumeInfo']['industryIdentifiers']
        # if identifiers_list empty, then no isbn10, go to next entry
        if len(identifiers_list) != 0:
            # Note entry may still not has ISBN10
            index = 0
            while isbn10 == -1 and index < len(identifiers_list):
                id = identifiers_list[index]
                if id['type'] == 'ISBN_10':
                    isbn10 = int(id['identifier'])
                index+=1

    return isbn10
