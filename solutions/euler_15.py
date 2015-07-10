def findPath(xcoo, ycoo, full, new):
	return full[ycoo-1][xcoo]+new[xcoo-1]
import time
start_time = time.time()

# ----------------------------------------------------------------
# figure out that the connected inputs must be added together as you traverse the matrix.

# _ _
#|_ _|
#|_ _|

# create array of (20 + 1) x (20 + 1)
start = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
datar = [start]
for j in xrange (1,21):
	temp = [1]
	for i in xrange (1,21):
		temp.append(findPath(i,j,datar, temp))
	datar.append(temp)
print datar

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------