import requests
msg = {"suggested_temperature": 22}
r = requests.post("http://localhost:7000/set-temp", json=msg)
print("Response:", r.json())