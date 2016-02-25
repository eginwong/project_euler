import math
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

import time
import sys
start_time = time.time()

# ----------------------------------------------------------------
# have a counter for natural numbers
counter = 1
for i in xrange(2, 100000000000000000):
	counter += i
	if (len(factors(counter)) > 500):
		print counter
		print("--- %s seconds ---" % (time.time() - start_time))
		sys.exit()

# ----------------------------------------------------------------
