from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import pymongo

app = Flask(__name__)
api = Api(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["food"]
mycol = mydb["openfood"]

class Food(Resource):
    def get(self):
        return {'prot': 21}
class Food_bar(Resource):
    def get(seld,code):
        result = mycol.find({'code' : code},{'product_name' : 1,'nutriments':1})
        return result[0]

api.add_resource(Food, '/food')
api.add_resource(Food_bar, '/food/<code>')

if __name__ == '__main__':
     app.run(host='192.168.1.59',port='5002')
