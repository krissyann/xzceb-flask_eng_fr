from machinetranslation import translator
from flask import Flask, render_template, request
import json
# # import machinetranslation
# from machinetranslation import frenchToEnglish, englishToFrench
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
<<<<<<< HEAD
    # Write your code here
    return translator.englishToFrench(textToTranslate)
    # return "Translated text to French" 
=======
    translation = translator.english_to_french(textToTranslate)
    return translation
>>>>>>> cd490f45844cbb01f2b68972266e43673a164b01

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
<<<<<<< HEAD
    # Write your code here
    return translator.frenchToEnglish(textToTranslate)
    # return "Translated text to English" 

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
=======
    translation = translator.french_to_english(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

>>>>>>> cd490f45844cbb01f2b68972266e43673a164b01
