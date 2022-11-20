# webhook post from python
# https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python

import requests
import json

def send_webhook():
    url = "http://192.168.1.188"
    data = {
    "braviaTVControl": {
        "config": {
            "ip": "192.168.1.129",
            "pin": "1175",
            "nickname": "DeviceName",
            "deviceID": "123456890"
        },
        "event": {
            "value": "turn_on",
            "args": ""
        }
    }
    }
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    print(result)
send_webhook()