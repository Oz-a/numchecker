def gcd_iter(a,b):
  '''
  a:int
  b:int

  returns the greates common denominator of a and b
  '''
  iterval = min(a,b)
  while not (a%iterval == 0 and b%iterval ==0):
    iterval -= 1

  print(f"The gcd of {a} and {b} is {iterval}.")
