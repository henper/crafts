'''
Created on Nov 13, 2019

@author: eponhik
'''
import json
import requests
from time import strftime
from authentication import Authentication

fh = open('client_credentials.json','r')
cc = json.loads(fh.read())
fh.close()
key = cc.get('key').encode('utf-8')
secret = cc.get('secret').encode('utf-8')

auth = Authentication(key=key, secret=secret)

ulleviNorraId = 9021014007171000
url = 'https://api.vasttrafik.se/bin/rest.exe/v2/'
api = 'departureBoard'

date = strftime('%Y-%m-%d')
time = strftime('%H:%M')

params = {'id': str(ulleviNorraId), 'date': date, 'time': time, 'format': 'json'}

response = requests.get(url+api, params=params, headers = {'Authorization' : 'Bearer ' + auth.getValidToken()})

print(response.content.decode('utf-8'))
