import time
start_time = time.time()

# ----------------------------------------------------------------

#fibonnacci
start = [1,1]
x = 0
# to get length of digits in a num
while len(str(x)) != 1000:
    x = start[len(start) - 1] + start[len(start) - 2]
    start.append(x)
    print x

print "The answer is: " + str(len(start))

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
