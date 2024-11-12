import math

def solve(swimmers, usedSwimmers, criteria):
    if criteria == 4:
        return 0
    
    minTime = math.inf
    for i in range(len(swimmers)):
        if i not in usedSwimmers:
            usedSwimmers.add(i)
            result = solve(swimmers, usedSwimmers, criteria + 1) + swimmers[i][criteria]
            minTime = min(minTime, result)
            usedSwimmers.remove(i)
    
    return minTime

N = int(input())
swimmers = []
for i in range(N):
    swimmers.append([int(x) for x in input().split()])

swimmerSet = set()
for criteriaIndex in range(4):
    listToSort = list(map(lambda tup: (tup[1][criteriaIndex], tup[0]), enumerate(swimmers)))
    listToSort.sort(key=lambda tup: tup[0])
    for tup in listToSort[0:4]:
        swimmerSet.add(tup[1])
    
swimmersToConsider = []

for index in swimmerSet:
    swimmersToConsider.append(swimmers[index])

print(solve(swimmersToConsider, set(), 0))