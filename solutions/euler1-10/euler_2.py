base_num=raw_input("What's your max number?")
sum=0
i=1
j=2
temp=0
while j <= int(base_num): 
  if j%2 == 0:
    sum = sum + j
  temp = j
  j = i + j
  i = temp
print sum
