from flask import Flask, render_template, request
from translator.translator import english_to_french, french_to_english

app = Flask(__name__)
app.template_folder = 'templates'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english():
    french_text = request.form.get('frenchText')
    translation = french_to_english(french_text)
    return render_template('index.html', translation=translation)

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french():
    english_text = request.form.get('englishText')
    translation = english_to_french(english_text)
    return render_template('index.html', translation=translation)


if __name__ == '__main__':
    app.run(debug=
            True, port=5557)
