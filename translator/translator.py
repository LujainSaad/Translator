from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])

def english_to_french(text):
    translation = translator.translate(text, src='en', dest='fr')
    return translation.text

def french_to_english(text):
    translation = translator.translate(text, src='fr', dest='en')
    return translation.text
