
'''
Given a book title, make a REST API call to the Google
Books API and get the ISBN-10 of the first search result
that has an ISBN-10. If no ISBN-10 is found,
-1 is returned.

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
