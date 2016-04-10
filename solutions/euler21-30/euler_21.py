import time
from math import ceil
start_time = time.time()

# ----------------------------------------------------------------

def d (num):
    dRes = 0
    # https://projecteuler.net/thread=21 Improved performance by using ceiling
    for i in range(1,int(ceil(num/2)+1)):
        if num%i == 0:
            dRes += i
    return dRes

def ami (num):
    if num == d(d(num)) and d(num) != d(d(num)):
        return True

sumRes = 0
for i in xrange(1, 10000):
    if ami(i):
        sumRes += i

print "The answer is: " + str(sumRes) + "."

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
