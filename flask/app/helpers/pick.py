def pick(customDict, dataArray):
  myDict = {}
  for key in range(len(dataArray)):
      myDict[dataArray[key]] = customDict[dataArray[key]] if dataArray[key] in customDict else ''
  return myDict
