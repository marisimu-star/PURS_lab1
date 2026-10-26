import requests

url = "http://192.168.83.5/login"

# 1. Test s ISPRAVNIM podacima
print("--- ISPRAVNI PODACI ---")
tocno = {'username': 'PURS', 'password': '1234'}
odgovor1 = requests.post(url, json=tocno)

print("Status:", odgovor1.status_code)
print("Odgovor:", odgovor1.text)


# 2. Test s NEISPRAVNIM podacima
print("\n--- NEISPRAVNI PODACI ---")
netocno = {'username': 'PURS', 'password': 'KRIVO'}
odgovor2 = requests.post(url, json=netocno)

print("Status:", odgovor2.status_code)
print("Odgovor:", odgovor2.text)
