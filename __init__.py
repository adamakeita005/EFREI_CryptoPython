from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)


key = 7580b9636ac84da59a43b106bf6e9cd0
fernet = Fernet(key)

@app.route("/")
def index():
    return "Bonjourtoutlemonde"

@app.route("/encrypt/<value>")
def encrypt(value):
    token = fernet.encrypt(value.encode())
    return f"Valeur encryptée : {token.decode()}"

@app.route("/decrypt/<token>")
def decrypt(token):
    try:
        value = fernet.decrypt(token.encode()).decode()
        return f"Valeur décryptée : {value}"
    except:
        return "Erreur de décryptage"
