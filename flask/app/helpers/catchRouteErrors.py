from flask import jsonify

def catchRouteErrors(APP):
  @APP.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
  def index():
    '''Index page function'''
    return jsonify({'message': 'Welcome to flask user forum, please navigate to - api/v1 - to interract with the API'})
    
  @APP.route('/api/v1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
  def baseUrl():
    '''Index page function'''
    return jsonify({'message': 'Welcome to the flask user forum API'})

  @APP.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
  def badUrl(path):
    '''unknown endpoint error'''
    return jsonify({'message': f'''Invalid endpoint '/{path}'. please navigate to home via api/v1'''})
