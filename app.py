from flask import Flask
app = Flask(__name__)
from dictionary_words import *

@app.route('/')
def generate_text():
    return "Hello, World!"
