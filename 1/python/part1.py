import sys

filename = sys.argv[1]
inp = open(filename, 'r')
lines = inp.readlines()

maxSum = 0
currSum = 0
for line in lines:
    if line == "\n":
        maxSum = max(currSum, maxSum)
        currSum = 0
    else:
        currSum += int(line)
print(maxSum)