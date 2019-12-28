from flask import jsonify

class auth:
  def login(self):
    return jsonify({'message': 'Login successful'})

  def signup(self, data):
    return jsonify({'username': data.username, 'password': data.password})
