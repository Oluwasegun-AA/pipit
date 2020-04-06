def omit(customDict, keysArray):
  for key in keysArray:
    del customDict[key]
  return customDict

def pick(customDict, keysArray):
  myDict = {}
  for key in range(len(keysArray)):
      myDict[keysArray[key]] = customDict[keysArray[key]] if keysArray[key] in customDict else ''
  return myDict

def cleanData(data):
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

def normalize(data):
  dataArr= []
  if type(data) == list:
    for item in data:
      dataArr.append(cleanData(item))
    return dataArr
  else:
    return cleanData(data)
