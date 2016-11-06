import time
start_time = time.time()

# ----------------------------------------------------------------
# WHAT IS THE UPPER BOUND? THAT'S THE KEY.9^5 'cause I think of 99999. But that sum is 295245 (5*9^5), which means it can be a 6 digit number.
# We then need 6*9.5 to set a reasonable upper bound, which is 354294.
# This helped: http://www.mathblog.dk/project-euler-30-sum-numbers-that-can-be-written-as-the-sum-fifth-powers-digits/
maxFives = 0
for i in xrange(2, 355000):
    temp = [int(d) for d in str(i)]
    sum = 0
    for j in temp:
        sum+=j**5
    if sum == i: maxFives+= i
print maxFives
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
