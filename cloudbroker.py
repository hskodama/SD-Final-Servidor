from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://admin:sd1234@ds159184.mlab.com:59184/sd"
mongo = PyMongo(app)

PROV_URL = 'http://127.0.0.1:5000/'
@app.route('/')
def init():
    return 'Welcome to SD'

@app.route('/provedor/cadastrar/<pid>',methods=['POST'])
def init_provedor(pid):
    data = request.get_json()
    mongo.db['vm'].insert_one(
        {
            'pid': pid,
            'vcpu': data['vcpu'],
            'ram': data['ram'],
            'hd': data['hd'],
            'preco':data['preco'],  
            'usando': ['False']
        })

    return jsonify({'Ok': True})

@app.route('/provedor/search/<pid>', methods=['POST'])
def search_provedor(pid):
    data = request.get_json()
    retorno = {}
    busca = mongo.db['vm'].find(
        {
            'pid': [pid]
        }
    )

    for resultados in busca:
        json_data = json.dumps(resultados)

    return json_data

@app.route('/search',methods=['POST'])
def search_vm():
    data = request.get_json()
    busca = mongo.db['vm'].find(
        {
            'vcpu':{'$gte': data['vcpu']},
            'ram': {'$gte': data['ram']},
            'hd': {'$gte': data['hd']},
            'usando': ['False']
        }
    )
    for resultados in busca:
        print(resultados['_id'])

    return jsonify({'Ok': True})


