import time
start_time = time.time()

# ----------------------------------------------------------------
def spiral(n):
    reps = (n - 1) / 2
    tot = 1
    running = 1
    increment = 2
    while reps > 0:
        for i in xrange(1,5):
            running +=increment
            tot += running
        reps-=1
        increment+=2
    return tot

print spiral(1001)
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
