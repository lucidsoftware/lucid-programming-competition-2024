# Does not pass test case 9

from collections import deque

days = [int(day) for day in input().split()]
costs = [int(cost) for cost in input().split()]

seven, thirty = deque(), deque()
total = 0

for day in days:
    while seven and seven[0][0] <= day-7:
        seven.popleft()
    if not seven:
        seven.append((day, total + costs[1]))

    while thirty and thirty[0][0] <= day-30:
        thirty.popleft()
    if not thirty:
        thirty.append((day, total + costs[2]))

    total = min(total+costs[0], seven[-1][1], thirty[-1][1])

print(total)
