def combination(n, r)
  a = n - r
  keep_N = n
  keep_R = r
  n = 1
  r = 1
  
  for Range_N in range(1, keep_N+1):
    n *= Range_N
  
  for Range_R in range(1, a+1):
    r *= Range_R
  
  ans = n/r
  
  r = 1
  
  for Range_R in range(1, keep_R+1):
    r *= Range_R
  
  fans = ans/r
  
  return fans
    
