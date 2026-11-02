
import requests

url = "http://127.0.0.1:5000/temperatura"

# 1. POST zahtjev - slanje temperature
podaci = {
    "temperatura": 67
}

odgovor = requests.post(url, json=podaci)

print("POST zahtjev:")
print("Status:", odgovor.status_code)
print("Odgovor:", odgovor.text)


# 2. GET zahtjev - dohvat zadnje temperature
odgovor = requests.get(url)

print("\nGET zahtjev:")
print("Status:", odgovor.status_code)
print("Odgovor:", odgovor.json())
