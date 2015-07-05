import time
import sys

start_time = time.time()

base_num=raw_input("What's your num?")
squared_nat=0
sum_squared=0
for i in xrange(1,int(base_num)+1):
  squared_nat = squared_nat + i **2
  sum_squared = sum_squared + i
print sum_squared**2, squared_nat
print (sum_squared**2 - squared_nat)
print("--- %s seconds ---" % (time.time() - start_time))
sys.exit()
