import time
import math
start_time = time.time()

# ----------------------------------------------------------------
# Get a subset of 1 - 100 and figure out the list from there.
# Got some help figuring this one out. Important to look at the remainder and play with modulo
maxCount = 0
ans = 0
for i in xrange(2,1000):
    cycle = 0
    mod = []
    temp = 1%i
    while not temp in mod:
        mod.append(temp)
        temp = (10*temp)%i
        if temp == 0:
            break
        else:
            cycle+=1
    if cycle > maxCount:
        maxCount = cycle
        ans = i
print str(ans) + " has " + str(maxCount) + " cycles."

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
