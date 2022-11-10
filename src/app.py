import json
import random
from flask import Flask
from flask import request
from flask import jsonify
from db.db_manager import load_orders, save_new_order, read_orders

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/ordenar', methods=['POST'])
def new_order():
    req_json = request.json
    print(req_json)
    save_new_order(req_json)
    return req_json

    # print(req_json)

@app.route('/api/v1/ordenar', methods=['POST'])
def new_order2():
    req_json = request.json
    print(req_json)
    save_new_order(req_json)
    return req_json


@app.route('/api/v1/ordenar', methods=['GET'])
def get_orders():
    ordenes = load_orders()
    print(ordenes)
    return ordenes

@app.route('/api/v1/ordenar2', methods=['GET'])
def get_order():
    ordenesBase = read_orders()
    print(ordenesBase)
    return ordenesBase






@app.route('/api/v1/ordenar/<orden_id>', methods=['GET'])
def get_order_by_id():
    return None


if __name__ == '__main__':
    app.run()
