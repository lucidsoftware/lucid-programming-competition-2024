days = [int(ea) for ea in input().split(' ')]
costs = [int(ea) for ea in input().split(' ')]

memo = {}
def findCheapestPathToEnd(i, expirationDate):
    k = (i, expirationDate)
    if k not in memo:
        if i == len(days):
            res = 0
        elif expirationDate > days[i]:
            res = findCheapestPathToEnd(i+1, expirationDate)
        else:
            res = min(costs[0] + findCheapestPathToEnd(i+1, days[i] + 1),
                   costs[1] + findCheapestPathToEnd(i+1, days[i] + 7),
                   costs[2] + findCheapestPathToEnd(i+1, days[i] + 30))
        memo[k] = res
    return memo[k]

print(findCheapestPathToEnd(0, 0))
