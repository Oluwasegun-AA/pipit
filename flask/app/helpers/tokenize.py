import os
import jwt
from flask import jsonify
import datetime

class Tokenize:
  @staticmethod
  def encrypt(data):
    dataDict = {}
    for a, b in data.items():
      dataDict[a] = f'{b}'
    dataDict['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
    values = jsonify(dataDict)
    return (jwt.encode(dataDict, os.getenv('SECRETE'), algorithm=os.getenv('JWT_ALGORITHM'))).decode('utf-8')
  
  @staticmethod
  def decrypt(token):
    try:
      return jwt.decode(token, os.getenv('SECRETE'), algorithms=[os.getenv('JWT_ALGORITHM')])
    except:
      return {'error': 401, 'error': 'Unauthorized, invalid token'}
