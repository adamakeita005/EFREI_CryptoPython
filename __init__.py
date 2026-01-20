from flask import Flask, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# clé de test (suffisant pour le TP)
key = Fernet.generate_key()
fernet = Fernet(key)

@app.route("/")
def index():
    return "API CryptoPython OK"

@app.route("/encrypt/<value>")
def encrypt(value):
    token = fernet.encrypt(value.encode())
    return token.decode()

from flask import Flask, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# clé de test (suffisant pour le TP)
key = Fernet.generate_key()
fernet = Fernet(key)

@app.route("/")
def index():
    return "API CryptoPython OK"

@app.route("/encrypt/<value>")
def encrypt(value):
    token = fernet.encrypt(value.encode())
    return token.decode()
