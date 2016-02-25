import time
import sys

def check(num):
  print num
  for i in [5, 7, 9, 11, 13, 16, 17, 19]:
    if(num%i==0):
      if(i==19):
        return 1
    else:
      return 0

start_time = time.time()
test=20
while True:
  if check(test) == 1:
    print 'the final number is ' + str(test)
    print("--- %s seconds ---" % (time.time() - start_time))
    sys.exit()
  else:
    test += 20