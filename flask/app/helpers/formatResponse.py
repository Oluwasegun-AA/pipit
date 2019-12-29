
class formatResponse():

  @staticmethod
  def single(descriptions, data):
    response = {}
    columns = [col[0] for col in descriptions]
    for key in range(len(columns)):
      response[columns[key]] = data[key]
    return response
  
  @staticmethod
  def multiple(descriptions, data):
    response = {}
    responseArray = []
    columns = [col[0] for col in descriptions]
    for item in range(len(data)):
      for key in range(len(columns)):
        response[columns[key]] = data[item][key]
      responseArray.append(response)
    return responseArray
