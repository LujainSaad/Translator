from flask import Flask, render_template
from translator.translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/translate/french-to-english/<text>')
def translate_french_to_english(text):
    translation = french_to_english(text)
    return translation

@app.route('/translate/english-to-french/<text>')
def translate_english_to_french(text):
    translation = english_to_french(text)
    return translation

if __name__ == '__main__':
    app.run()
