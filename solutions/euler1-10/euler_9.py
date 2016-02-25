def triplet(a,b,c):
  if(c > b and b > a and (a**2 + b**2 == c**2)):
    return True
  else:
    return False

def addit(a,b,c):
  if(a + b + c == 1000): 
    return True
  return False

import time
start_time = time.time()

# ----------------------------------------------------------------

# a must be less than 332
# b must be less than 500.
# a > b
# b > c
for a in xrange(0,332):
  for b in xrange(a, 500):
    for c in xrange(b, 500):
      if(addit(a,b,c)):
        if(triplet(a,b,c)):
          print a*b*c, a, b, c
          print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
