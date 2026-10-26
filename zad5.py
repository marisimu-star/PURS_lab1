import requests

url = "http://192.168.83.5/temperatura"

# JSON poruka s proizvoljnom vrijednosti temperature
podaci = {"temperatura": 666}

# Slanje POST zahtjeva
odgovor = requests.post(url, json=podaci)

# Ispis rezultata
print("Statusni kod:", odgovor.status_code)
print("Tijelo odgovora:", odgovor.text)
