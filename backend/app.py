import os
from Modules.db_connect import *
from flask import Flask, render_template, jsonify


domain = os.getenv('Domain')
port = os.getenv('Port')

app = Flask(__name__)

data = [{"name": "vaibhav","age": 24, "nationality": "Indian"},{"name": "rishi","age": 89, "nationality": "UP"},{"name": "Alex","age": 22, "nationality": "USA"}]

@app.route("/")
def home():
  return render_template("home.html",data=data)

@app.route("/api/data")
def json_data():
  return jsonify(data)

@app.route("/api/products")
def json_product():
  return jsonify(fetch_all_products())

@app.route("/api/data/<int:id>")
def get_data():
  return 0

@app.route("/products")
def show_product():
  products = fetch_all_products()
  return render_template("products.html",proudcts=products)

if __name__ == "__main__":
  app.run(debug=True)