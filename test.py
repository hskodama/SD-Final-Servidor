from flask import request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
db = SQLAlchemy()

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'cloud broker',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/provider/initialize', methods=['POST'])
def initialize_connection():
    return "initialize"

@app.route('/customer_request', methods=['POST'])
def customer_request():
    received_data = json.load(request.files['datas'])
    vCPU = received_data['vCPUs']
    RAM = received_data['RAM']
    HD = received_data['HD']
    print (vCPU, RAM, HD)
    #preco =
    return "token"


    