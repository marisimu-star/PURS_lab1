
import requests

url = "http://127.0.0.1:5000/temperatura"

# Slanje nekoliko temperatura
requests.post(url, json={"temperatura": 20})
requests.post(url, json={"temperatura": 25})
requests.post(url, json={"temperatura": 30})

# DELETE zahtjev - brisanje temperature s indeksom 1
odgovor = requests.delete(url, params={"id": 4})

print("Status:", odgovor.status_code)
print("Odgovor:", odgovor.text)

# GET zahtjev - provjera zadnje temperature
odgovor = requests.get(url)

print("Zadnja temperatura:", odgovor.json())
