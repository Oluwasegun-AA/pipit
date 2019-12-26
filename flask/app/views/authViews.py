from flask import jsonify
from flask_restful import Resource
from app.helpers.request import getRequest

class auth(Resource):
  def post(self):
    data = getRequest()
    return jsonify({'message': 'Login successful',  'data':data})

class signup(Resource):
  def post(self):
    data = getRequest()
    return jsonify({'message': 'signup successful', 'data': data})
