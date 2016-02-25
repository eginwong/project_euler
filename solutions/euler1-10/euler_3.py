def check(max):
    for j in range(3,i):
      if i%j == 0:
        return 0
    return 1

import math
base_num=raw_input("What's your max number?")
max=1
for i in range (2, int(math.ceil(int(base_num)**0.5))):
  if int(base_num)%i == 0:
    if check(i) == 1:
      max = i
print max