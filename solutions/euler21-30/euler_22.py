import time
import csv

def char_position(letter):
    return ord(letter.lower()) - 96

def name_score(name):
    name_array = list(name)
    sumName = 0
    for i in range(0, len(name_array)):
        sumName += char_position(name_array[i])
    return sumName

start_time = time.time()

#read in the csv.
names = []
with open('p022_names.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for i, line in enumerate(reader):
        names = line

names.sort()
print "######################################################################################################################"

total = 0
for i in range(0, len(names)):
    total += (i+1)*name_score(names[i])

print "The answer is: " + str(total) + "."
# ----------------------------------------------------------------

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
