from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask.globals import request

#These are commented out for production
#app = Flask(__name__)
#CORS(app)


app = Flask(__name__, static_url_path='/', static_folder='../frontend/build')
app.config['CORS_HEADERS'] = 'Content-Type', 'Access-Control-Allow-Origin'

with open("server/data/products.json") as data:
    data = json.load(data)


shoppingData = {
    "shoppingcart": [

    ]
}

@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/products")
@cross_origin()
def products():
    return data


@app.route("/api/shoppingcart", methods=['GET'])
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



