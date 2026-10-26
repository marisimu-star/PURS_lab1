import requests

url = "http://192.168.83.5/temperatura"

# Slanje GET zahtjeva
odgovor = requests.get(url)

# Dohvaćanje zaglavlja Content-Type
tip_sadrzaja = odgovor.headers.get("Content-Type", "")
print("Content-Type je:", tip_sadrzaja)

# Provjera je li format application/json
if "application/json" in tip_sadrzaja:
    # Pretvaranje odgovora u JSON i dohvaćanje ključa 'temperatura'
    podaci = odgovor.json()
    print("Temperatura iznosi:", podaci.get("temperatura"))
else:
    print("Odgovor nije u JSON formatu!")
