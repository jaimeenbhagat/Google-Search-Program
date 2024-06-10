#100 searches per day
import requests

API_KEY = open('API_KEY').read()
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read()

search_query = input("What is your query?")

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': search_query,
    'key': 'Enter your api key here',
    'cx': 'Enter your search engine id',
    #'searchType': 'image'
    #'dateRestrict': '2016-01-01:2016-12-31'
}

response = requests.get(url,params=params)
results = response.json()['items']


for item in results:
    print(item['link'])