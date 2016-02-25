import time
start_time = time.time()

#Method declaration
def calculateMax(i):
    largest = []
    nextL = []
    x = len(i)-1
    print (len(i[x])-1)
    for y in xrange(len(i[x])-1):
        largest.append(max(i[x-1][y]+i[x][y], i[x-1][y] + i[x][y+1]))
    print largest

    for x in reversed(range(1, len(i)-1)):
        for y in xrange(len(i[x])-1):
            nextL.append(max(i[x-1][y]+largest[y], i[x-1][y] + largest[y+1]))
        largest = nextL
        nextL = []
        print largest

    print("The largest sum is: " + str(largest[0]))

# ----------------------------------------------------------------
# Make pyramid of numbers.

obj = {}
myList = []

with open('euler_17.txt') as f:
    content = f.readlines()

for i in xrange(len(content)):
    myList = content[i].rstrip('\n').split(' ')

    for j in range(0, len(myList)):
        myList[j] = int(myList[j])
    obj[i] = myList

#loop through each row in triangle

calculateMax(obj)

print("--- %s seconds ---" % (time.time() - start_time))
# ----------------------------------------------------------------
