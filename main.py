from flask import Flask, render_template, request
import os
from AEScipher import AESCipher
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def enkripsi():
    if request.method == 'POST':
        input_text = request.form['plaintext']
        input_key = request.form['key']
        cipher = AESCipher(input_key)
        encrypted = cipher.encrypt(input_text)
        return render_template('enkripsi.html', submit=True, ciphertext=encrypted)
    return render_template('enkripsi.html', submit=False, variabel=1234)


@app.route('/dekripsi', methods=['POST', 'GET'])
def dekripsi():
    if request.method == 'POST':
        input_text = request.form['plaintext']
        input_key = request.form['key']
        cipher = AESCipher(input_key)
        decrypted = cipher.decrypt(input_text)
        return render_template('dekripsi.html', submit=True, plaintext=decrypted)
    return render_template('dekripsi.html', submit=False, variabel=1234)


app.run()
