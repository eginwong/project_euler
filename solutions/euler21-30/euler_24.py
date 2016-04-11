import time
import itertools
start_time = time.time()

# ----------------------------------------------------------------
relTotal = list(map("".join, itertools.permutations('0123456789')))
absTotal = [int(i) for i in relTotal]

absTotal.sort()
print absTotal[999999]

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
