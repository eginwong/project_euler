import math
def isPrime(num):
	if (num > 1):
	  # check for factors
	  for i in xrange(2,int(math.ceil(num**0.5)) + 1):
	    if (num % i) == 0:
	      return False
	  return True

import sys
count=1
base_num=1
primeNum=base_num
print '1 2'
while True:
	for i in range (base_num, 100000000):
	  if isPrime(i):
	    count += 1
	    primeNum = i
	    print str(count) + ' ' + str(primeNum)
	    if count == 10001:
	    	sys.exit()