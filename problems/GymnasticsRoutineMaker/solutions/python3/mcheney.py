"""
Do a DFS of every possible combination of moves, memoizing by move and depth
"""

from collections import defaultdict

DEBUG = False

N = int(input())
moves = []
moveScore = {}
nextMoves = defaultdict(set)
for n in range(N):
    line = input().split(" ")
    move = line[0]
    score = line[1]
    percent = int(line[2]) / 100
    for preMove in line[3:]:
        nextMoves[preMove].add(move)
    moveScore[move] = int(score) * percent

dfsMemo = {}
# Returns the highest score you can get starting here
def dfs(move, depth):
    key = (move, depth)
    if key not in dfsMemo:
        if depth == 9:
            ans = moveScore[move], [move]
        else:
            maxScore = 0
            maxScorePath = []
            for nextMove in nextMoves[move]:
                newScore, path = dfs(nextMove, depth + 1)
                if newScore >= maxScore:
                    maxScore = newScore
                    maxScorePath = path
            ans = maxScore + moveScore[move], [move] + maxScorePath
        dfsMemo[key] = ans
    return dfsMemo[key]


bestS = 0
bestP = []
for startMove in nextMoves["start"]:
    s, p = dfs(startMove, 0)
    if len(p) < 10:
        continue
    if s > bestS:
        bestS = s
        bestP = p
if len(bestP) != 10:
    print("not length 10!")
    exit(1)
print("{:.3f}".format(bestS / 10))
if DEBUG: print(*bestP)
