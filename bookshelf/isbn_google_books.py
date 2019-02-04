
'''
Given a book title, make a REST API call to the Google
Books API and get the ISBN-10 as a string of the first search result
that has an ISBN-10. If no ISBN-10 is found,
empty string is returned.

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
then empty string is returned.

Return:
Empty string if no ISBN
'-1' if HTTPError
else return ISBN
'''
import urllib.error
from urllib.request import urlopen
import json

def get_isbn_10(title: str) -> str:

    isbn10 = ''
    titleSplit = title.split(' ')
    formattedTitle = ''
    for i in range(len(titleSplit)):
        formattedTitle = formattedTitle + titleSplit[i]
        if i < (len(titleSplit) - 1):
            formattedTitle = formattedTitle + '+'
    # Now, formattedTitle is same as title, but
    # delimited with + instead of spaces
    baseURL = r'https://www.googleapis.com/books/v1/volumes?q='
    apiKey = 'YOURGOOGLEAPIKEYHERE'
    apiURL = baseURL + formattedTitle + '&key=' + apiKey
    try:
        request = urlopen(apiURL)
        contents = request.read()
        # type of contents should be bytes
        # now parse from JSON into python dict
        parsed = json.loads(contents)

        # Find ISBN, should be under
        # industryIdentifiers
        list_of_entries = parsed['items']
        for entry in list_of_entries:
            has_industryIdentifiers = True
            volDict = entry['volumeInfo']
            if 'industryIdentifiers' not in list(volDict.keys()):
                has_industryIdentifiers = False
            if has_industryIdentifiers == True:
                identifiers_list = entry['volumeInfo']['industryIdentifiers']
                # if identifiers_list empty, then no isbn10, go to next entry
                if len(identifiers_list) != 0:
                    # Note entry may not have ISBN10
                    index = 0
                    while isbn10 == '' and index < len(identifiers_list):
                        id = identifiers_list[index]
                        if id['type'] == 'ISBN_10':
                            isbn10 = id['identifier']
                        index+=1
    except urllib.error.HTTPError:
        return '-1'

    return isbn10
