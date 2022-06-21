def iter_pow (base, exp):
  '''
  input:base and exp, two integers
  returns the exponential of base integer.
  '''
  ans = 1
  while exp > 0:
    ans *= base
    exp -= 1

  return ans
