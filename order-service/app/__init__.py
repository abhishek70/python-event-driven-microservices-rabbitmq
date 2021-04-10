from dataclasses import dataclass

import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pika, json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://dev:dev@order-db/order'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    db.UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/')
@app.route('/health')
def health():
    return jsonify(status='up')


@app.route('/api/products')
def products():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/order', methods=['POST'])
def order(id):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    req = requests.get('http://cms-web:8080/api/users')
    data = req.json()
    try:
        product_user = ProductUser(user_id=data['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()
        properties = pika.BasicProperties('order_placed')
        channel.basic_publish(exchange='', routing_key='order', body=json.dumps(id), properties=properties)
    except:
        abort(400, 'Product already purchased')

    return jsonify({'status': 'success', 'message': 'order placed'})
