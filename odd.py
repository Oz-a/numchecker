def odd_check(x):
  '''
  input: gets an integer
  returns a print statement telling if the integer is odd.
  '''
  if x%2==0:
    print(f"{x} is not odd.")
  elif x%2 != 0:
    print(f"{x} is odd.")

odd_check(23)