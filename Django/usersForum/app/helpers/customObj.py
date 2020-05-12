from rest_framework.utils.serializer_helpers import ReturnList

def pick(data, keysArray):
  myDict = {}
  for key in range(len(keysArray)):
      myDict[keysArray[key]] = data[keysArray[key]] if keysArray[key] in data else ''
  return myDict

def omit(data, keysArray):
  try :
    data.keys()
    for key in keysArray:
      del data[key]
    return data
  except :
    newArr = []
    for item in data:
      newItem = item
      for key in keysArray:
        del newItem[key]
      newArr.append(newItem)
    return newArr
