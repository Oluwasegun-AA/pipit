from flask import jsonify, request

def getRequest():
  if request.headers['Content-Type'] == 'application/json':
    return request.get_json(force=True)
  else:
    return request.form
    