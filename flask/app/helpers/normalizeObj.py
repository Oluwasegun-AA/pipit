def normalize(data):
  dataDict = {}
  if type(data) == dict:
    for a, b in data.items():
      if type(b) == dict:
        for x, y in b.items:
          b[x] = f'{y}'
        dataDict[a] = f'{b}'
      else: dataDict[a] = f'{b}'
    return dataDict
  else: return data