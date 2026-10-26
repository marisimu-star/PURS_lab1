import requests

url = "http://192.168.83.5/temperatura"

# Definiranje URL (query) parametra id
parametri = {"id": 1}

# Slanje DELETE zahtjeva s parametrima
odgovor = requests.delete(url, params=parametri)

# Ispis rezultata
print("Statusni kod:", odgovor.status_code)
print("Tijelo odgovora:", odgovor.text)
