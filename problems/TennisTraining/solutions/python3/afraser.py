from functools import lru_cache

days = [int(x) for x in input().split()]
costs = [int(x) for x in input().split()]

@lru_cache(maxsize=None)
def solve(index):
    if index >= len(days):
        return 0
    day = days[index]
    seventhDay = None
    counter = index + 1
    while(counter < len(days) and days[counter] < day + 30):
        if days[counter] >= day + 7 and seventhDay == None:
            seventhDay = counter
        counter = counter + 1

    if seventhDay == None:
        seventhDay = counter
    
    thirtiethDay = counter
    oneDayPass = costs[0] + solve(index + 1)
    sevenDayPass = costs[1] + solve(seventhDay)
    thirtyDayPass = costs[2] + solve(thirtiethDay)
    return min(oneDayPass, sevenDayPass, thirtyDayPass)

print(solve(0))