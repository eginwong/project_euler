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
    # if (num == dRes):
        # "Perfect" numbers
        # print "Perfect, number is: " + str(num) + " and Res is: " + str(dRes)
    if (num < dRes):
        # print "Abundant, number is: " + str(num) + " and Res is: " + str(dRes)
        return True
    # elif (num > dRes):
        # print "Deficient, number is: " + str(num) + " and Res is: " + str(dRes)

abundantNum = []
for i in xrange(12, 28123):
    if d(i):
        abundantNum.append(i)

print abundantNum

dictSum = {}
for k in xrange(1, 28123):
    dictSum[k] = False

print dictSum

for i in xrange (0, len(abundantNum)):
    for j in xrange(i, len(abundantNum)):
        total = abundantNum[i] + abundantNum[j]
        if total <= 28123:
            dictSum[total] = True
        else:
            break

res = 0
for key in dictSum:
    if not dictSum[key]:
        res += key

print res

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
