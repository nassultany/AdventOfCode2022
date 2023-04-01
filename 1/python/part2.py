import sys

N = 3
topN = [0] * N

def placeSum(calories: int):
    for i in range(N):
        if calories > topN[i]:
            for j in range(N-1,i, -1):
                topN[j] = topN[j-1]
            topN[i] = calories
            break

filename = sys.argv[1]
inp = open(filename, 'r')
lines = inp.readlines()

currSum = 0
for line in lines:
    if line == "\n":
        placeSum(currSum)
        currSum = 0
    else:
        currSum += int(line)
print(sum(topN))