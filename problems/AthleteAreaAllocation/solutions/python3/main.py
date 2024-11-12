import math
import sys

# Get all inputs
n = int(input())

flags = []
for _ in range(n):
    XY = [int(s) for s in input().split()]
    flags.append(XY)



# Sort flag coordinates by x position
flags.sort(key = lambda coord: coord[0])



# Divide and conquer functions

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute force compares all points inside the indices
def compare_all_inside(lower_index, upper_index):
    inner_min_distance = sys.maxsize
    for i in range(lower_index, upper_index + 1): # Upper bound is exclusive
        for j in range(lower_index, upper_index + 1):
            if i != j:
                inner_min_distance = min(inner_min_distance, dist(flags[i], flags[j]))
    return inner_min_distance

# Gets minimum distance between all points inside the indices. Uses the current minimum distance and the position of the middle point to optimize.
def get_strip_min(current_min, middle_point, lower_index, upper_index):
    strip_flags = []
    strip_min = current_min

    # Get flags in strip closer than current_min to the x value of the middle point
    for i in range(lower_index, upper_index + 1):
        if abs(flags[i][0] - middle_point[0]) < current_min:
            strip_flags.append(flags[i])
    
    strip_flags.sort(key = lambda coord: coord[1]) # Sort strip flags by y value

    for i in range(len(strip_flags)):
        for j in range(i + 1, len(strip_flags)):
            if strip_flags[j][1] - strip_flags[i][1] >= strip_min:
                break
            else:
                strip_min = min(strip_min, dist(strip_flags[i], strip_flags[j])) 
    return strip_min

def recursive_compare(lower_index, upper_index):
    if upper_index - lower_index < 3: # If there are 2 or 3 points, just compare all of them
        return compare_all_inside(lower_index, upper_index)

    # Get middle point
    middle_index = ((upper_index - lower_index) // 2) + lower_index
    middle_point = flags[middle_index]

    # Separately handle the left and right half of your current range
    left_half_min = recursive_compare(lower_index, middle_index)
    right_half_min = recursive_compare(middle_index + 1, upper_index)

    # Get smallest of both halves
    current_min = min(left_half_min, right_half_min)

    # Get smallest inside strip that's within `current_min` of the vertical line = middle_point.y
    strip_min = get_strip_min(current_min, middle_point, lower_index, upper_index)

    return min(current_min, strip_min)



# Execute and output
min_distance = recursive_compare(0, n - 1)
print(round(min_distance, 3))