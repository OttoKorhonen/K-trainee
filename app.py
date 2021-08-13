from flask import Flask, session, jsonify
import json
from flask.globals import request

app = Flask(__name__)
app.secret_key = "liik3deef0equo7vieng9weim8geeJ"


def open_data():
    with open("server/data/products.json") as data:
        data = json.load(data)
    return data


def get_product(id: int):
    data = open_data()
    for product in data["Products"]:
        if id == int(product["id"]):
            return product
    raise ValueError("Id not found")


@app.route("/api/products")
def products():
    return jsonify(open_data())


@app.route("/api/shoppingcart", methods=['GET'])
def shoppingcart():
    result = {
        "products": [],
        "total": 0,
        "status": "Success"
    }
    current_cart = session.get("shoppingcart", {})

    total = 0

    for productId in current_cart:
        p_id = get_product(int(productId))
        p_id["count"] = current_cart[productId]
        result["products"].append(p_id)
        total += p_id["price"] * p_id["count"]

    result["total"] = total

    return jsonify(result)


@app.route("/api/shoppingcart", methods=['POST'])
def add_item_in_cart():

    result = {
        "products": [],
        "total": 0,
        "status": "Success"
    }

    current_cart = session.get("shoppingcart", {})

    new_Item = request.get_json()

    try:
        new_product = get_product(new_Item["id"])
        count = int(new_Item.get("count", 1))
        if count > 0:
            current_cart[new_product["id"]] = count
            session["shoppingcart"] = current_cart
        else:
            pass

    except ValueError:
        result["status"] = "Product not found"
    except KeyError:
        result["status"] = "Product id couldn't be found"

    total = 0

    for productId in current_cart:
        p = get_product(int(productId))
        p["count"] = current_cart[productId]
        result["products"].append(p)
        total += p["price"] * p["count"]

    result["total"] = total

    return jsonify(result)
