
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# Globalna lista za spremanje temperatura
temperature = []


# 1. zadatak - pocetna stranica
@app.route("/", methods=["GET"])
def pocetna():
    return "Početna stranica"


# 2. zadatak - login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return "Stranica za prijavu"

    podaci = request.get_json()

    username = podaci.get("username")
    password = podaci.get("password")

    if username == "PURS" and password == "1234":
        return redirect("/")

    else:
        return redirect("/login")


# 3. zadatak - POST temperatura
@app.route("/temperatura", methods=["POST"])
def postavi_temperaturu():

    podaci = request.get_json()

    if not podaci or "temperatura" not in podaci:
        return "Niste upisali ispravan ključ", 404

    temperature.append(podaci["temperatura"])

    return "Uspješno ste postavili temperaturu", 201


# 4. zadatak - GET temperatura
@app.route("/temperatura", methods=["GET"])
def dohvati_temperaturu():

    if len(temperature) == 0:
        return "Nema spremljenih temperatura", 404

    return jsonify({
        "temperatura": temperature[-1]
    })


# 5. zadatak - DELETE temperatura
@app.route("/temperatura", methods=["DELETE"])
def obrisi_temperaturu():

    id = request.args.get("id")

    if id is None or not id.isdigit():
        return "Upisali ste neispravan ključ", 404

    id = int(id)

    if id < 0 or id >= len(temperature):
        return "Upisali ste neispravan ključ", 404

    temperature.pop(id)

    return "Uspješno ste obrisali temperaturu", 202


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
