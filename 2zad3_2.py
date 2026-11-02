
import requests

url = "http://127.0.0.1:5000/temperatura"

podaci = {
    "temperatura": 25
}

odgovor = requests.post(url, json=podaci)

print("Status:", odgovor.status_code)
print("Odgovor:", odgovor.text)
