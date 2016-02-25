base_num=raw_input("What's your max number?")
sum=0
for i in  range (0, int(base_num)):
  if(i%3 == 0 or  i%5==0):
    sum = sum + i
print sum
