import time
start_time = time.time()

# ----------------------------------------------------------------
# http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
# As the challenge here is not about finding prime numbers, I'll be using a nice clean option.
def is_prime(a):
    return all(a % i for i in xrange(2, a))

def calculate(n,a,b):
    return (n*n + a*n + b)

maxN = 0
product = 0
for a in xrange(-1000,1000):
    # Because negative numbers cannot be prime, by Googling.
    for b in xrange(2,1000):
        if(is_prime(b)):
            i = 0
            while(is_prime(abs(calculate(i,a,b)))):
                i+=1
            if i > maxN:
                print str(a) + " and " + str(b) + " have made " + str(i) + " consecutive primes."
                maxN = i
                product = a*b
print "maxN is " + str(maxN) + " and product is " + str(product)

# print "The largest product is " + str(product) + " with " + str(maxN) + " primes."
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
