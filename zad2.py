import requests

# Definiranje URL-a profesorskog računala
url = "http://192.168.83.5"

try:
    # Slanje HTTP GET zahtjeva na putanju '/'
    response = requests.get(url)
    
    # 1. Ispis statusnog koda
    print(f"--- STATUSNI KOD ---")
    print(f"{response.status_code} {response.reason}\n")
    
    # 2. Ispis svih zaglavlja (Headers)
    print(f"--- ZAGLAVLJA (HEADERS) ---")
    for kljuc, vrijednost in response.headers.items():
        print(f"{kljuc}: {vrijednost}")
    print("\n")
    
    # 3. Ispis tijela odgovora (Body)
    print(f"--- TIJELO ODGOVORA (BODY) ---")
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Dogodila se pogreška prilikom povezivanja: {e}")
