import math
def isPrime(num):
        if (num > 1):
          # check for factors
          for i in xrange(2,int(math.ceil(num**0.5)) + 1):
            if (num % i) == 0:
              return False
          return True


import time
start_time = time.time()

# ----------------------------------------------------------------
sum = 2
totNum = 2000000
for i in xrange(2,totNum):
  if isPrime(i):
    sum += i
print sum
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
