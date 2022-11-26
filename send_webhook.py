# webhook post from python
# https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python

import requests
import json

def send_webhook():
    url = "http://127.0.0.9/"
    data = {
    "debug" : {
        "action": "selfDestr"
        }
}
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    print(result)
send_webhook()