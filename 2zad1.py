from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pocetna():
    return "Početna stranica"

@app.route("/login", methods=["GET"])
def login():
    return "Stranica za prijavu"

if __name__ == "__main__":
    app.run(debug=True)