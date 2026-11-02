
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


# 3. zadatak - temperatura
@app.route("/temperatura", methods=["POST"])
def postavi_temperaturu():

    podaci = request.get_json()

    if not podaci or "temperatura" not in podaci:
        return "Niste upisali ispravan ključ", 404

    temperature.append(podaci["temperatura"])

    return "Uspješno ste postavili temperaturu", 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
