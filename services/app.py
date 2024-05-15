import sys
sys.path.insert(0,'lib')


import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from pathlib import Path


dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
domain = os.getenv('Domain')
port = os.getenv('Port')
print(domain,port)


app = Flask(__name__)


data = [{"name": "vaibhav","age": 24, "nationality": "Indian"},{"name": "rishi","age": 89, "nationality": "UP"},{"name": "Alex","age": 22, "nationality": "USA"}]

@app.route("/")
def home():
  return render_template("Home.html",data=data)

@app.route("/api/data")
def json_data():
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)