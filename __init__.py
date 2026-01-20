from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)


key = b'XxkYkXb2sQ6e7kJ7VnZbKq3W2U0l7y8M1QpT9YxA0s='
fernet = Fernet(key)

@app.route("/")
def index():
    return "API Crypto OK"

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
