from flask import Flask, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# clé de test (suffisant pour le TP)
key = gAAAAABpbvOViTlMNHxknf3qSx1l1IZDub3qjxMqUMHfreBkPTPtQixN_XKTgg_AmWYHxNmHoudEab072JBulbaZ2sM8qfFtoB1lCBiCtGKYGmyE8FiI-64=
fernet = Fernet(key)

@app.route("/")
def index():
    return "Bonjourtoutlemonde"

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
    return "Bonjourtoutlemonde"

@app.route("/encrypt/<value>")
def encrypt(value):
    token = fernet.encrypt(value.encode())
    return token.decode()
