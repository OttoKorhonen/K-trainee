from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask.globals import request

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type', 'Access-Control-Allow-Origin'

with open("../data/products.json") as data:
    data = json.load(data)


shoppingData = {
    "shoppingcart": [

    ]
}


@app.route("/api/products")
@cross_origin()
def products():
    return data


@app.route("/shoppingcart", methods=['GET'])
@cross_origin()
def shoppingcart():
    return shoppingData


@app.route("/api/shoppingcart", methods=['POST'])
@cross_origin()
def get_data_from_front():
    requestedData = request.get_json()
    dataToJson = json.dumps(requestedData, indent=4, sort_keys=True)
    shoppingData["shoppingcart"].append(dataToJson)
    return shoppingData


if __name__ == "__main__":
    app.run(debug=True, port=5001)
