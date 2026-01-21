from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)

# Clé unique pour la session
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/decrypt/<value>')
def decrypt(value):
    try:
        decrypted_value = cipher.decrypt(value.encode())
        return decrypted_value.decode()
    except Exception:
        return "Erreur : valeur impossible à décrypter"
