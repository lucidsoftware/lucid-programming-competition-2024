"""
This solution uses a binary search, checking the slope at each
point to decide whether to cut left or right.

Slope is calculated by comparing the value at x to the value
at x + DELTA_FOR_SLOPE (i.e. some very small number).
"""

from math import sin


def getJumpHeight(x, f):
    return (6 - 2 * f * sin(x / 2) - 2 * f * sin(x / 5) - 2 * f * sin(x / 7)) * (0.9 + (1 + sin(x * f / 3)) / 20)

N = int(input())
Fs = [float(ea) for ea in input().split(" ")]
M = int(input())
milestones = []
for m in range(M):
    L, R, H = [float(ea) for ea in input().split(" ")]
    milestones.append((L, R, H))

DELTA_FOR_SLOPE = .000001
DELTA_THRESHOLD_FOR_SEARCH = .000000000000000001
def getSlope(x, f):
    h1 = getJumpHeight(x, f)
    h2 = getJumpHeight(x + DELTA_FOR_SLOPE, f)
    if h1 < h2:
        return 1
    if h1 > h2:
        return -1
    return 0

scores = []
for n in range(N):
    S = 0
    F = Fs[n]
    for m in range(M):
        L, R, H = milestones[m]
        delta = (R - L) / 2
        x = L + ((R - L) / 2)
        while delta > DELTA_THRESHOLD_FOR_SEARCH:
            delta = delta / 2
            slope = getSlope(x, F)
            if slope == 1:
                x += delta
            elif slope == -1:
                x -= delta
            else:
                break
        localMax = getJumpHeight(x, F)
        if localMax > H:
            S += localMax
    scores.append((n+1, S))

scores = sorted(scores, key = lambda x: x[1], reverse=True)

for score in scores:
    print(score[0])
    print("{:.6f}".format(score[1]))
