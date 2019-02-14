import cleanup
import tokenize
import word_count
import sample
import sentence

from flask import Flask

app = Flask(__name__)

@app.route('/')
def generate_text():
    return "Hello, World!"

if __name__ == '__main__':
    # code to run when file is executed
