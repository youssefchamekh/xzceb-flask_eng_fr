from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
    def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    res = translator.englishToFrench(textToTranslate)
    # Write your code here
    return res

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    res = translator.frenchToEnglish(textToTranslate)
    # Write your code here
    return res

@app.route("/")
def renderIndexPage():
    # Write the code to render template
   return render_template('index')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

