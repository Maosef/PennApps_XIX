


from gcloud_ocr import detect_text

path = "books_rotated.jpg"

texts = detect_text(path)

print(texts[0].description)

texts = texts.split('\n')

#filter bad titles
#get ISBN number and book contents
for title in texts:
        
