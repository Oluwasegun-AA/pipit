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
    return response

  def patch(self, id):
    data = pick(getRequest(), ['username', 'email', 'firstName', 'lastName'])
    response = Users.updateUser(str(id), data)
    return response

  def delete(self, id):
    response = Users.deleteUser(str(id))
    return response

  def post(self):
    req = getRequest()
    data = Auth.signup(req)
    return data

class GetAllUser(Resource):
  def get(self):
    response = Users.getAllUser()
    return response

class VerifyUser(Resource):
  def patch(self, id):
    response = Users.verifyUser(str(id))
    return response

class makeAdmin(Resource):
  def patch(self, id):
    req = pick(getRequest(), ['isAdmin'])
    response = Users.makeAdmin(str(id), req)
    return response