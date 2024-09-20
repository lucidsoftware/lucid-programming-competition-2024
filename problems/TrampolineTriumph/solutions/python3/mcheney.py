"""
This solution uses a ternary search.
"""

from math import sin


def getJumpHeight(x, f):
    return (6 - 2 * f * sin(x / 2) - 2 * f * sin(x / 5) - 2 * f * sin(x / 7)) * (0.9 + (1 + sin(x * f / 3)) / 20)

THRESHOLD_TO_STOP_TERN_SEARCH = .0000000001

def findLocalMax(a, b, f):
    if abs(getJumpHeight(a, f) - getJumpHeight(b, f)) <= THRESHOLD_TO_STOP_TERN_SEARCH:
        return (a + b) / 2
    m1 = a + (b - a) / 3
    m2 = a + (b - a) * 2 / 3
    if getJumpHeight(m1, f) < getJumpHeight(m2, f):
        return findLocalMax(m1, b, f)
    else:
        return findLocalMax(a, m2, f)

N = int(input())
Fs = [float(ea) for ea in input().split(" ")]
M = int(input())
milestones = []
for m in range(M):
    L, R, H = [float(ea) for ea in input().split(" ")]
    milestones.append((L, R, H))

scores = []
for n in range(N):
    S = 0
    F = Fs[n]
    for m in range(M):
        L, R, H = milestones[m]
        localMaxX = findLocalMax(L, R, F)
        localMax = getJumpHeight(localMaxX, F)
        if localMax > H:
            S += localMax
    scores.append((n+1, S))

scores = sorted(scores, key = lambda x: x[1], reverse=True)

for score in scores:
    print(score[0])
    print("{:.6f}".format(score[1]))
