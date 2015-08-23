import time
start_time = time.time()


# ----------------------------------------------------------------
# create a list of the numbers!

#1-9 = 36
total = (3+3+5+4+4+3+5+5+4)

#10-19 = 70
tens = (3+6+6+8+8+7+7+9+8+8)

#20-99 = 748
hundreds = 8*36 +10*(6+6+5+5+5+7+6+6)

#100-999
# hundred and = 10 * 9 hundreds * 99 times per hundred
# 1-9 00 is done about 100 times 
# each digit from 1-99 is done through 9*(total + tens + hundreds)
thousands = 99*9*10 + 7*9 + total*100 + 9*(total+tens+hundreds)

# one thousand = 11
one_more = 11

print total + tens + hundreds+ thousands + one_more

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------