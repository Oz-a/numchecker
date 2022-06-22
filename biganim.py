def biggest(adict):
  '''
  get a dictionary composed of list values
  returns the key of the longest list
  '''
  tempdict = {}
  for k in adict.keys():
    tempdict[k] = len(adict[k])

  biggest = max(tempdict.values())

  for k in adict:
    if len(adict[k]) == biggest:
      return k
      




#Test = biggest({'B': [15], 'u': [10, 15, 5, 2, 6]})
#print(Test)
