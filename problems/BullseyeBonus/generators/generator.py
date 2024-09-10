# Pass in values to stdin to determine N, M, and test number
#
# Example:
# 100 500 3
# This creates a test case with N=100, M=500 in the test file 03.in

import random
import math

def two_distinct_random_numbers(rangeStart, rangeEnd):
    initialRandom = random.randint(rangeStart, rangeEnd)
    secondRandom = random.randint(rangeStart, rangeEnd)
    while secondRandom == initialRandom:
        secondRandom = random.randint(rangeStart, rangeEnd)
    
    return (initialRandom, secondRandom)

[N, M, testNum] = map(lambda x: int(x), input().split(' '))
filename = "{:02}.in".format(testNum)
filePrefix = "/home/afraser/lucid/lucid-programming-competition-2024/problems/BullseyeBonus/tests/"
file = open(filePrefix + filename, "w")
file.write(" ".join(map(lambda x: str(x), [N, M])) + "\n")

archers = []
for i in range(N):
    #num = math.floor(random.normalvariate(50, 50 / 4))
    num = random.randint(-10, 10)
    archers.append(num)

# print(min(archers))
# print(max(archers))

file.write(" ".join(map(lambda x: str(x), archers)) + "\n")

for j in range(M):
    (bullseye, loser) = two_distinct_random_numbers(1, len(archers))
    rangeLength = random.randint(0, len(archers) - 1)
    start = random.randint(1, len(archers) - rangeLength)
    ending = "\n"
    if j == M - 1:
        ending = ""
    file.write(" ".join(map(lambda x: str(x), [bullseye, loser, start, start + rangeLength])) + "\n")