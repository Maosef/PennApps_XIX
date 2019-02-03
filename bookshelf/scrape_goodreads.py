'''
Given title, make API call to GoodReads and
return the work ID.

Returns 0 if not found
'''
import xml.etree.ElementTree as ET
import requests



def get_goodreads_id(title: str) -> int:
    id = 0

    baseURL = r'https://www.goodreads.com/search.xml?key=vfjQv3RyzRKtbRfFjX7Q&q='
    titleSplit = title.split(' ')
    formattedTitle = '+'.join(titleSplit)
    url = baseURL + formattedTitle

    try:
        response = requests.get(url)
    
        tree = ET.fromstring(response.content)
        id_element = tree.find(r'./search/results/work/id')
        id_string = ET.tostring(id_element, encoding='utf-8').decode('utf-8')
        first_num = id_string.find('>') + 1
        last_num = id_string.find('<', 1)
        id = int(id_string[first_num: last_num])
        
    except:
        # Handle error
        pass
    
    return id
