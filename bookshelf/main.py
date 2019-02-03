
from gcloud_ocr import detect_text
from isbn_google_books import get_isbn_10
from scrape_goodreads import get_goodreads_id 
from rec_books import get_recs

path = "books_rotated.jpg"

texts = detect_text(path)

texts = texts[0].description

texts = texts.split('\n')

#filter bad titles, get related books from Goodreads
for title in texts:
    #print(title)
    work_id = get_goodreads_id(title) 
    rec_list = get_recs(str(work_id))
    if rec_list == -1 or rec_list == None: continue    
    for rec in rec_list:
        print(rec)


