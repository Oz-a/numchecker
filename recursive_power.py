def rec_pow(base, exp):
  '''
  base: int or float
  exp: int >= 0 

  returns: int or float: base^exp
  '''
  if exp == 0:
    return 1
  else:
    return base * rec_pow(base, exp-1)

print(rec_pow(5,5))