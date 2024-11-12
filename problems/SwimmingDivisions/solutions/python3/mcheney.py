import sys

sys.setrecursionlimit(100000)

N = int(input())

winnerOfDivision = dict()

def getAndMaybeSetTopLevelWinner(name, newWinner = None):
    if winnerOfDivision[name] == name:
        if newWinner is not None:
            winnerOfDivision[name] = newWinner
        return winnerOfDivision[name]
    res = getAndMaybeSetTopLevelWinner(winnerOfDivision[name], newWinner)
    winnerOfDivision[name] = res
    return res

for n in range(N):
    name = input()
    winnerOfDivision[name] = name
while True:
    command = input().split(' ')
    if command[0] == "END":
        break
    if command[0] == "COMPETITION":
        M = int(command[1])
        names = [input()]
        for m in range(M-1):
            names.append(input())
        for name in names:
            oldWinner = getAndMaybeSetTopLevelWinner(name, names[0])
            winnerOfDivision[oldWinner] = names[0]
    if command[0] == "REQUEST":
        name = command[1]
        print(getAndMaybeSetTopLevelWinner(name))
