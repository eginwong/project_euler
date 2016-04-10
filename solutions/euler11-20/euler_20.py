import time
import math
start_time = time.time()

# ----------------------------------------------------------------

result = math.factorial(100)
result_array = [int(i) for i in str(result)]
total = 0
for i in range(0, len(result_array)):
    total += result_array[i]

print "The answer is: " + str(total) + ". "

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
