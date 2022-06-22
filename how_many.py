
def how_many(adict):
  '''
  input: dictionary, where all values are lists

  returns the number of elements in the dictionary
  '''
  counter = 0
  for k in adict.values():
    for i in k:
      counter += 1

  return counter


#Test = how_many({'B': [15], 'u': [10, 15, 5, 2, 6]})
#print(Test)

