import math

# Helper functions
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Get all inputs
n = int(input())

flags = []
for _ in range(n):
    XY = [int(s) for s in input().split()]
    flags.append(XY)

# Iterate over every pair
min_distance = None
for i in range(len(flags)):
    for j in range(len(flags)):
        if i != j:
            current_distance = dist(flags[i], flags[j])
            if min_distance is None:
                min_distance = current_distance
            else:
                min_distance = min(min_distance, current_distance)

print(round(min_distance, 3))