import math
n = int(input())
flags = [None] * n
for i in range(n):
    flags[i] = list(map(int, input().split()))

minimum_distance = math.inf
for i in range(n):
    for j in range(i):
        distance = (((flags[i][0] - flags[j][0]) ** 2) + ((flags[i][1] - flags[j][1]) ** 2)) ** 0.5
        minimum_distance = min(minimum_distance, distance)

print("{:.3f}".format(minimum_distance))
