from decouple import config
import datetime
import jwt
import json

class Tokenize:
  @staticmethod
  def encrypt(data):
    decode_key = config('SECRETE')+ str(data['id']).lower().replace('e', config('SECRETE'))
    signatures = { "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600), "iat": datetime.datetime.utcnow() }
    values = dict({**data, **signatures})
    return (jwt.encode(values, decode_key, algorithm=config('JWT_ALGORITHM'))).decode('utf-8')
  
  @staticmethod
  def decrypt(token, decode_key, verify=True):
      return jwt.decode(token, decode_key, algorithm=config('JWT_ALGORITHM'), verify=verify)
