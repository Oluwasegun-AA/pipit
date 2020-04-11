import os
import jwt
import datetime
from app.helpers.normalizeObj import normalize

class Tokenize:
  @staticmethod
  def encrypt(data):
    dataDict = normalize(data)
    signatures = { "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600), "iat": datetime.datetime.utcnow() }
    values = dict({**dataDict, **signatures})
    return (jwt.encode(values, os.getenv('SECRETE'), algorithm=os.getenv('JWT_ALGORITHM'))).decode('utf-8')
  
  @staticmethod
  def decrypt(token):
    try:
      return jwt.decode(token, os.getenv('SECRETE'), algorithms=[os.getenv('JWT_ALGORITHM')])
    except:
      return dict({'error': 401, 'error': 'Unauthorized, invalid token'}), 401
