from flask import Flask, request
from flask_cors import CORS
import json
from config import db

app = Flask(__name__)
CORS(app)

@app.get("/")
def hello_world():
    return "Hello World"

@app.get("/api/version")
def version():
    version = {"name": "products-api", "version": 1} 
    return json.dumps(version)

products = []


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def read_products():
    cursor = db.products.find({})
    catalog = []
    for item in cursor:
        catalog.append(fix_id(item))
    return json.dumps(catalog)


@app.post("/api/products")
def save_product():
    product = request.get_json()
    # Validation

    db.products.insert_one(product)
    # products.append(product)
    return json.dumps(fix_id(product))

#path parameter (<int:index>)
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"index: {index}")

    if index >= 0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist"

app.run(debug=True, port=5001)