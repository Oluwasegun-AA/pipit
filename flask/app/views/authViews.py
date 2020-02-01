from flask import jsonify
from flask_restful import Resource
from app.helpers.request import getRequest
from app.models.authModels import authModel

Auth = authModel()

class auth(Resource):
  def post(self):
    req = getRequest()
    data = Auth.login(req)
    return jsonify(data)

class signup(Resource):
  def post(self):
    req = getRequest()
    data = Auth.signup(req)
    return jsonify(data)
