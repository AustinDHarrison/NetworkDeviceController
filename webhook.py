import requests
import json

webhook_url = 'http://192.168.1.188:80/webhook'

data = {'TestOne': 'Test1',
        'TestTwo': 'Test2'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})