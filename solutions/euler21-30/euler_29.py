import time
start_time = time.time()

# ----------------------------------------------------------------
master = {}
for a in xrange(2,101):
    for b in xrange(2,101):
        if not a**b in master:
            master[a**b] = 1
print len(master.keys())
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
