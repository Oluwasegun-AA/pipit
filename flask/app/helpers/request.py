from flask import request

def getRequest():
  if request.headers['Content-Type'] == 'application/json':
    return dict(request.get_json(force=True))
  else:
    return dict(request.form)
