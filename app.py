from flask import Flask, session, jsonify
import json
from flask.globals import request

app = Flask(__name__)
app.secret_key="liik3deef0equo7vieng9weim8geeJ"

def openData():
    with open("server/data/products.json") as data:
        data = json.load(data)
    return data

# def checkData(object:dict):
#     data = openData()
#     productNames = []
#     for productName in data["Products"]:
#         productNames.append(productName["name"])

#     try:
#         if object["name"] in productNames and object["name"] != "Shovel":
#             return True
#         else:
#             raise ValueError
#     except ValueError:
#         print("Ooops!... Object name not allowed or it is out of stock")

def get_product(id:int):
    data = openData()
    for product in data["Products"]:
        if id == int(product["id"]):
            return product
    raise ValueError("Id not found")


@app.route("/api/products")
def products():
    return openData()


@app.route("/api/shoppingcart", methods=['GET'])
def shoppingcart():
    return jsonify(session.get("shoppingcart", []))


@app.route("/api/shoppingcart", methods=['POST'])
def storeData():
    
    currentCart = session.get("shoppingcart", [])
    newItem = request.get_json()
    currentCart.append(newItem)
    session["shoppingcart"] = currentCart
    return jsonify(session["shoppingcart"])
    



"""
curl -X POST http://127.0.0.1:5000/api/shoppingcart -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
   """