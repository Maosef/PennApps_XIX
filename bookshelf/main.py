
from gcloud_ocr import detect_text
from isbn_google_books import get_isbn_10
from rec_books import get_related

path = "books_rotated.jpg"

texts = detect_text(path)

texts = texts[0].description

texts = texts.split('\n')

#filter bad titles
#get ISBN number and book contents
for title in texts:
    print(title)
    if not all(ord(c) < 128 for c in title): continue

    isbn = get_isbn_10(title)
    print(title, isbn)
    #rec_list = get_related(isbn)
    
    #for rec in rec_list:
    #    print(rec)


