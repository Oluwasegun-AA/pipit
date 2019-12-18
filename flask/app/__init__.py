import os
from flask import Flask, jsonify
from instance.config import (Development, Testing, Production)

def getEnvironmentConfig():
  if os.getenv('FLASK_ENV') == 'development':
    return Development
  elif os.getenv('FLASK_ENV') == 'production':
    return Production
  else: return Testing


APP = Flask(__name__)
APP.config.from_object(getEnvironmentConfig())

@APP.route('/api/v1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def index():
    '''Index page function'''
    return jsonify({'message': 'Welcome to flask, please navigate to "api/v1" to interract with the API'})
