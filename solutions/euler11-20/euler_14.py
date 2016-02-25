def collatz(n):
	if (n%2==0):
		return (n/2)
	else:
		return (3*n + 1)

import time
import string
start_time = time.time()

# ----------------------------------------------------------------
# have a counter for natural numbers

maxCount = 0
ans = 0
for i in range(500001,1000000, 2):
	n = i
	longest = 1
	temp = i
	while (n != 1):
		longest += 1
		n = collatz(n)
	if(longest > maxCount):
		maxCount = longest
		ans = temp

print maxCount, ans
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------