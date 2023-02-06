import requests
import json


response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

res = response.json()['items']

for data in res:
    print('data: ', data)
    print('title: ', data['title'])
    print('link: ', data['link'])