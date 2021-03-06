from flask import Flask, jsonify, request
from convModelFolder.convBlueprint import convBlueprint
from languageModelFolder.language_model_blueprint import languageModelBlueprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_response():
    return jsonify({
        'msg':
        'Try sending a HTTP POST request to the /convModel endpoint with\
        a RGB image attachment, or a GET request to /languageModel endpoint'
    })


app.register_blueprint(convBlueprint, url_prefix='/convModel')
app.register_blueprint(languageModelBlueprint, url_prefix='/languageModel')

if __name__ == "__main__":
    app.run()
