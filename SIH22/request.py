import requests
import json

promise = requests.post("https://xerebro-dd93f-default-rtdb.firebaseio.com/", json.dumps(f"100"))
print(promise)