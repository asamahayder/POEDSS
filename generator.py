import json.encoder
import time
import urllib.request
import urllib.parse

"""while True:
    d = {"value": 5}
    data = urllib.parse.urlencode(d).encode("utf-8")
    req = urllib.request.Request("http://localhost:8081/randomInt")
    req.add_header("Content-type", "application/json")
    urllib.request.urlopen(req, data).read()

    time.sleep(2000)"""

"""import urllib.request
import json

reqUrl = 'http://localhost:8081/randomInt'
reqData = {"value": 5}
reqData = json.encoder(reqData)
headers = {
    'Content-Type': 'application/json'
}
method = 'POST'
req = urllib.request.Request(reqUrl, reqData, headers, method=method)
with urllib.request.urlopen(req) as res:
    body = json.load(res)"""

import requests
import time
import random

while True:
    number = random.randint(0, 9)
    r = requests.post('http://localhost:8081/randomInt', json={
        "value": number
    })
    print(f"Status Code: {r.status_code}, Response: {r.url}")
    time.sleep(2)

