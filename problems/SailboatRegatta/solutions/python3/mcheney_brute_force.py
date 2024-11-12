# This solution is too slow. It proves the test cases, and that Dijkstra's is necessary.
# DFS
# Memoize based on velocity, sail position, and recharge value
# Cut off before theoretical max (sail down, velocity of y=1 the whole time)

W, L, K = [int(ea) for ea in input().split(" ")]
currents = [[[0,0] for l in range(L)] for w in range(W)]
for l in range(L):
    pairs = input().strip().split(" ")
    for w, pair in enumerate(pairs):
        x, y = pair.split(",")
        currents[w][l] = [int(x), int(y)]

bssf = L + 1
memo = {}
# What is the shortest path the end
def dfs(x, y, xV, yV, sailIsUp, kRecharge, secondsSoFar):
    key = (x, y, xV, yV, sailIsUp, kRecharge)
    if key not in memo:
        if secondsSoFar > L or secondsSoFar > bssf:
            res = L + 1
        elif x < 0 or x >= W or y < 0:
            res = L + 1
        elif y >= L:
            res = 0
        else:
            if sailIsUp:
                xVOfCell, yVOfCell = currents[x][y]
                xV += xVOfCell
                yV += yVOfCell
            x += xV
            y += yV
            distanceWithFlippedSail = L + 1
            if kRecharge == 0:
                distanceWithFlippedSail = dfs(x, y, xV, yV, not sailIsUp, K - 1, secondsSoFar + 1)
            distanceWithSameSail = dfs(x, y, xV, yV, sailIsUp, max(0, kRecharge - 1), secondsSoFar + 1)
            res = 1 + min(distanceWithSameSail, distanceWithFlippedSail)
        memo[key] = res
    return memo[key]

for w in range(W):
    bssf = min(bssf, 1 + dfs(w, 0, 0, 1, True, 0, 0))
    bssf = min(bssf, 1 + dfs(w, 0, 0, 1, False, K - 1, 0))

print(bssf)
