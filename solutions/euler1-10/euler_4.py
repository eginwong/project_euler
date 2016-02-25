import sys
import time

def check(num):
  if(str(num)[::-1] == str(num)):
    return 1
  else:
    return 0

start_time = time.time()
limit = 999
base_num=999*999

for i in xrange (int(base_num), 1, -1):
  if(check(i) == 1):
    for j in xrange(limit, 1, -1):
      if(len(str(j)) == 3 and len(str(i/j)) == 3 and i%j == 0):
        print (i,j, i/j)
        print("--- %s seconds ---" % (time.time() - start_time))
     	sys.exit(0)
