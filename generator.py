import requests
import time
import random

"""while True:
    number = random.randint(0, 9)
    r = requests.post('http://localhost:8081/randomInt', json={
        "value": number
    })
    print(f"Status Code: {r.status_code}, Response: {r.url}")
    time.sleep(2)"""


r = requests.post('http://localhost:8600/card-status', json={
    "status": "Success"
})
print(f"Status Code: {r.status_code}, Response: {r.url}")

