#!/usr/bin/env python

from flask import Flask, jsonify, request
import datetime
import os
#from fake_catalog_model import products
from database_catalog_model import products

# Crear el objeto que representa la aplicacion web
APP = Flask(__name__)

# Endpoints proporcionados por este uServicio son
# GET /products (Todo el catálogo) 
# GET /products/<:sku> (Un producto en particular)
# POST /products (Crear un producto en particular) -> SKU


@APP.route('/products', methods=['GET'])
def all_products():
    return products.get_all_products()


@APP.route('/products', methods=['POST'])
def create_product():
    product = {
        'category': request.json['category'],
        'description': request.json['description'],
        'name': request.json['name'],
        'price': request.json['price']
    }
    product = products.insert_product(**product)
    return jsonify(product), 201



# GET /products/<:sku> (Un producto en particular)
# /products/ 
@APP.route('/products/<uuid:sku>', methods=['GET'])
def get_product_by_sku(sku):
    return products.get_product_by_sku(sku)


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=os.environ['PORT'])
