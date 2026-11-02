from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pocetna():
    return "Početna stranica"


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return "Stranica za prijavu"

    if request.method == "POST":

        podaci = request.get_json()

        username = podaci.get("username")
        password = podaci.get("password")

        if username == "PURS" and password == "1234":
            return redirect("/")

        else:
            return redirect("/login")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)