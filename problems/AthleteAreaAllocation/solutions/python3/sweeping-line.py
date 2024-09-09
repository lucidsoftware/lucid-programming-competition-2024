# This was taken from https://www.geeksforgeeks.org/closest-pair-of-points-using-sweep-line-algorithm

import math

# Get all inputs
n = int(input())

flags = []
for _ in range(n):
    XY = [int(s) for s in input().split()]
    flags.append(XY)

flags.sort(key=lambda p: p[0])

def closest_pair() :

    # Sort points according to x-coordinates

    # Array to store already processed points whose distance
    # from the current points is less than the smaller distance so far
    s = []

    squared_distance = 1e18
    j = 0

    for i in range(len(flags)):
        # Find the value of min_distance
        min_distance_so_far = math.ceil(math.sqrt(squared_distance))

        # Remove points that are too far from the current point
        while j <= i and flags[i][0] - flags[j][0] >= min_distance_so_far:
            s.pop(0)
            j += 1

        # Iterate over all such points and update the minimum distance
        k = 0
        while k < len(s):
            dx = flags[i][0] - s[k][0]
            dy = flags[i][1] - s[k][1]
            squared_distance = min(squared_distance, dx**2 + dy**2)
            k += 1

        # Insert the point into the SortedSet
        s.append([flags[i][0], flags[i][1]])
        s.sort(key=lambda p: p[0])

    return math.sqrt(squared_distance)

print(round(closest_pair(), 3))