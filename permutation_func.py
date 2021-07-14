def permutation(n, r):
  a = n - r
  keep_N = n
  n = 1
  r = 1
  
  for Range_N in range(0, keep_N):
    n *= Range_N
  
  for Range_R in range(0, a):
    r *= Range_R
  
  ans = n/r
  
  return ans
