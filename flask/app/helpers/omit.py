def omit(customDict, keysArray):
  for key in keysArray:
    del customDict[key]
  return customDict