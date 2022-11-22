from flask import render_template, request
from app import app 
import string

#from function import *


def encryptWithParams(message, key):
    alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c
    return encrypted_message


@app.route('/')
def home():
    return "Hello world!"

@app.route('/template')
def template():
    return render_template('home.html')
    
    
@app.route('/form')
def form():
    return render_template('form.html')
    
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        message1=form_data['Phrase']
        key1=int(form_data['Step'])
        encrypted_message = encryptWithParams(message1,key1)
        return render_template('data.html',result=encrypted_message)
    


