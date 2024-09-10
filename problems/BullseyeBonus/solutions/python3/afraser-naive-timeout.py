# Computes average by adding all of the numbers in range
# Runtime is O(N * M) since each query takes O(N) time to find the average
# This should time out on the largest N and M combinations

import math

[n, m] = [int(x) for x in input().split(' ')]
archers = [int(x) for x in input().split(' ')]

for i in range(m):
    [x, y, l, r] = [int(x) for x in input().split(' ')]
    average = math.floor(sum(archers[l - 1: r]) / (r + 1 - l))
    archers[x - 1] = archers[x - 1] + average
    archers[y - 1] = archers[y - 1] - average

print(archers.index(max(archers)) + 1)