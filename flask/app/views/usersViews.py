from flask import jsonify
from flask_restful import Resource
from app.helpers.request import getRequest
from app.models.authModels import authModel
from app.models.usersModels import UsersModel
from app.helpers.pick import pick

Auth = authModel()
Users = UsersModel()


class User(Resource):
  def get(self, id):
    user = getRequest()
    response = Users.getUser(str(id))
    return jsonify(response)

  def patch(self, id):
    data = pick(getRequest(), ['username', 'email', 'firstName', 'lastName'])
    response = Users.updateUser(str(id), data)
    return jsonify(response)

  def delete(self, id):
    response = Users.deleteUser(str(id))
    return jsonify(response)

  def post(self):
    req = getRequest()
    data = Auth.signup(req)
    return jsonify(data)

class GetAllUser(Resource):
  def get(self):
    response = Users.getAllUser()
    return jsonify(response)

class VerifyUser(Resource):
  def patch(self, id):
    response = Users.verifyUser(str(id))
    return jsonify(response)

class makeAdmin(Resource):
  def patch(self, id):
    req = pick(getRequest(), ['isAdmin'])
    response = Users.makeAdmin(str(id), req)
    return jsonify(response)