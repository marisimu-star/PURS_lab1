import requests

url = "http://127.0.0.1:5000/login"

podaci = {
    "username": "PURS",
    "password": "12345"
}

odgovor = requests.post(url, json=podaci)

print("Status:", odgovor.status_code)
print("URL:", odgovor.url)
print("Odgovor:", odgovor.text)
print("Preusmjeren:", odgovor.history)