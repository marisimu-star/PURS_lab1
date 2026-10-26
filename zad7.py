import requests

url = "https://api.ipify.org/?format=json"

# Slanje GET zahtjeva
odgovor = requests.get(url)

# Pretvaranje odgovora u JSON
podaci = odgovor.json()

# Dohvaćanje i ispis javne IP adrese iz ključa 'ip'
javna_adresa = podaci.get("ip")
print("Javna IP adresa računala je:", javna_adresa)