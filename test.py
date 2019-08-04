import requests
import json
url = "http://localhost:8000/articles/getG/"
# pk = "3"
postdata = {
    'title': 'title 2',
    'content': 'content 2',
    'author': 1
}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=postdata)
print(r.status_code)
print(r.text)
