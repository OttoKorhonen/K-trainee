from flask import Flask, session, jsonify
import json
from flask.globals import request
import datetime

app = Flask(__name__)
app.secret_key="liik3deef0equo7vieng9weim8geeJ"

def openData():
    with open("server/data/products.json") as data:
        data = json.load(data)
    return data

def checkData(object:dict):
    data = openData()
    productNames = []
    for productName in data["Products"]:
        productNames.append(productName["name"])

    try:
        if object["name"] in productNames and object["name"] != "Shovel":
            return True
        else:
            raise ValueError
    except ValueError:
        print("Ooops!... Object name not allowed or it is out of stock")
        


@app.route("/api/products")
def products():
    return openData()


@app.route("/api/shoppingcart", methods=['GET'])
def shoppingcart():
    return jsonify(session.get("shoppingcart", []))


@app.route("/api/shoppingcart", methods=['POST'])
def storeData():
    #tässä luetaan mitä käyttäjä haluaa lisätä koriin ja tarkistaa mitä korissa jo on
    #lisättävä tuote löytyy tuotelistalta
    session["shoppingcart"] = []
    requestedData = request.get_json()
    shoppingData = requestedData
    
    if checkData(shoppingData):
        session["shoppingcart"].append(shoppingData)
        print(session["shoppingcart"])
        return {"ef":shoppingData}
    else:
        return "Given object not allowed"


"""
curl -X POST http://127.0.0.1:5000/api/shoppingcart -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
   """