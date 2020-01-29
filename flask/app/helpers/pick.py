def pick(customDict, keysArray):
  myDict = {}
  for key in range(len(keysArray)):
      myDict[keysArray[key]] = customDict[keysArray[key]] if keysArray[key] in customDict else ''
  return myDict
