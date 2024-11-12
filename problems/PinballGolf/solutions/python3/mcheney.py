"""
Build a graph from the bumpers.
DFS to find probability of leaf node having Y = 0
"""
import math
import sys
from bisect import bisect_right, bisect_left
from collections import defaultdict

sys. setrecursionlimit(100000)

class Bumper:
    def __init__(self, X, Y, Ds):
        self.X = X
        self.Y = Y
        self.Ds = Ds

N, L = [int(ea) for ea in input().split(" ")]

bumpersByX = defaultdict(list)  # x -> list of bumpers, sorted by y

for n in range(N):
    X, Y, K = [int(ea) for ea in input().split(" ")]
    Ds = [int(ea) for ea in input().split(" ")]
    newBumper = Bumper(X, Y, Ds)
    bumpersByX[X].append(newBumper)

for x in bumpersByX.keys():
    bumpersByX[x] = sorted(bumpersByX[x], key=lambda b: b.Y)

# Consider the hole to be the target bumper
bumpersByX[0].append(Bumper(0, math.inf, []))

nextBumperMemo = dict()
def getNextBumper(x, y):
    # Get the bumper that ball hits next starting from x,y
    bumperId = (x,y)
    if bumperId not in nextBumperMemo:
        # Bisect search
        res = bisect_left(bumpersByX[x], y, key=lambda ea: ea.Y)
        if res >= len(bumpersByX[x]):
            nextBumperMemo[bumperId] = None
        else:
            nextBumperMemo[bumperId] = bumpersByX[x][res]

        # Linear search
        # res = None
        # for bumper in bumpersByX[x]:
        #     if bumper.Y > y:
        #         res = bumper
        #         break
        # nextBumperMemo[bumperId] = res
    return nextBumperMemo[bumperId]

# Ball starts at X = 0, Y = 0
root = Bumper(0, 0, [0])

dfsMemo = dict()
def dfs(cur):
    if cur not in dfsMemo:
        res = None
        if cur.Y == math.inf:
            # made it to the hole
            res = 1
        elif len(cur.Ds) == 0:
            # no more bumpers to hit
            res = 0
        else:
            p = 0
            k = 1 / len(cur.Ds)
            for d in cur.Ds:
                newBumper = getNextBumper(cur.X + d, cur.Y)
                if not newBumper:
                    # no bumper downhill of this Y
                    continue
                p += k * dfs(newBumper)
            res = p
        dfsMemo[cur] = res
    return dfsMemo[cur]

print("{:.6f}".format(dfs(root)))