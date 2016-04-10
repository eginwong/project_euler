import time
import datetime
from dateutil.relativedelta import relativedelta
start_time = time.time()

# ----------------------------------------------------------------

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

start_date = datetime.date(1901,1,1)
end_date = datetime.date(2000,12,31)

delta = relativedelta(months=+1)
d = start_date

sundayCounter = 0

while d <= end_date:
    if(d.weekday() == 6):
        sundayCounter += 1
    d += delta


print "################################"
print "There are " + str(sundayCounter) + " Sundays in this century."
print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
