from flask import Flask, session, jsonify
import json
from flask.globals import request

app = Flask(__name__)
app.secret_key = "liik3deef0equo7vieng9weim8geeJ"


def openData():
    with open("server/data/products.json") as data:
        data = json.load(data)
    return data


def get_product(id: int):
    data = openData()
    for product in data["Products"]:
        if id == int(product["id"]):
            return product
    raise ValueError("Id not found")


@app.route("/api/products")
def products():
    return jsonify(openData())


@app.route("/api/shoppingcart", methods=['GET'])
def shoppingcart():
    result = {
        "products": [],
        "total": 0,
        "status": "Success"
    }
    currentCart = session.get("shoppingcart", {})

    total = 0

    for productId in currentCart:
        p = get_product(int(productId))
        p["count"] = currentCart[productId]
        result["products"].append(p)
        total += p["price"] * p["count"]

    result["total"] = total

    return jsonify(result)


@app.route("/api/shoppingcart", methods=['POST'])
def add_item_in_cart():

    result = {
        "products": [],
        "total": 0,
        "status": "Success"
    }
    currentCart = session.get("shoppingcart", {})

    newItem = request.get_json()
    try:
        new_product = get_product(newItem["id"])
        # jos tuote on korissa ja siihen lisätään samaa tuotetta lisää
        # kori ei osaa ottaa huomioon aikaisempia tuotteita
        # apumuuttuja countille
        currentCart[new_product["id"]] = newItem.get("count", 1)
        session["shoppingcart"] = currentCart
    except ValueError:
        result["status"] = "Product not found"
    except KeyError:
        result["status"] = "Product id couldn't be found"

    total = 0

    for productId in currentCart:
        p = get_product(int(productId))
        p["count"] = currentCart[productId]
        result["products"].append(p)
        total += p["price"] * p["count"]

    result["total"] = total

    return jsonify(result)


"""
curl -X POST http://127.0.0.1:5000/api/shoppingcart -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
   """
