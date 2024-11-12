import math
n = int(input())
flags = [None] * n
for i in range(n):
    flags[i] = list(map(int, input().split()))

flags.sort(key=lambda p: p[0])

def get_distance(a, b):
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5

def get_minimum_distance_within_strip(strip, minimum_distance_so_far):
    count = len(strip)
    for i in range(count):
        for j in range(i):
            if abs(strip[i][1] - strip[i][1]) > minimum_distance_so_far:
                break
            else:
                minimum_distance_so_far = min(minimum_distance_so_far, get_distance(strip[i], strip[j]))

    return minimum_distance_so_far

def solve(left, right):
    count = right - left
    if count == 1:
        return float('inf')
    elif count == 2:
        return get_distance(flags[left], flags[left + 1])
    else:
        midpoint = left + (count // 2)
        minimum_distance_left = solve(left, midpoint)
        minimum_distance_right = solve(midpoint, right)
        minimum_distance_so_far = min(minimum_distance_left, minimum_distance_right)

        midpoint_x = flags[midpoint][0]
        strip = []
        for i in range(left, right):
            if abs(flags[i][0] - midpoint_x) <= minimum_distance_so_far:
                strip.append(flags[i])

        strip.sort(key=lambda p: p[1])
   
        return get_minimum_distance_within_strip(strip, minimum_distance_so_far)

minimum_distance = solve(0, n)

print("{:.3f}".format(minimum_distance))
