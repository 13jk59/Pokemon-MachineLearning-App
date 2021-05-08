from flask import Blueprint
from flask import jsonify
from flask import request
import os
import json
from keras.models import load_model
from ML_Model_Serving.languageModelFolder.model.languageModel import make_name

languageModelBlueprint = Blueprint('Language Model Blueprint', __name__)

with open(
        os.path.abspath('') +
        '/languageModelFolder/model/jsonified_items/jsonified_char_to_index.json',
        'r') as f:
    char_to_index = json.load(f)

with open(
        os.path.abspath('') +
        '/languageModelFolder/model/jsonified_items/jsonified_index_to_char.json',
        'r') as f:
    index_to_char = json.load(f)

model = load_model(
    os.path.abspath('') +
    '/languageModelFolder/model/trained_models/final_model.hdf5',
    compile=False)


@languageModelBlueprint.route('/', methods=['POST'])
def languageModel_rootAPIHandler():
    """
    This function is an API endpoint for the flask application that will respond to HTTP post requests to the 
    /languageModel/ endpoint. This function has the purpose of generating a variable number of pokemon names
    and returning them as a JSON object to the requestor. 
    """
    dataRecieved = request.get_json()
    temperature = round(float(dataRecieved["temperature"]), 2)
    number_to_generate = dataRecieved["number_to_generate"]
    predictedName = []
    for i in range(int(number_to_generate)):
        predictedName.append(
            make_name(model,
                      index_to_char,
                      char_to_index,
                      temperature=temperature,
                      max_seq_len=10))
    return jsonify({'predictedName': predictedName})
