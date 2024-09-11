from math import sqrt
from random import randint


def makeDisplacement():
    return randint(-20, 20) / 10


def makeDistance():
    return abs(makeDisplacement())


def notClose(left, right):
    return abs(left[1] - right[1]) > 0.1


def getX(name):
    return 0.3 if name == "Alice" else makeDisplacement()


def getY(name):
    return -0.4 if name == "Alice" else makeDisplacement()


def getDiameter(name):
    return 0.8 if name == "Alice" else makeDistance()


names = ["Alice", "Bob", "Carol", "David", "Eve"]
splashes = [(name, getX(name), getY(name), getDiameter(name)) for name in names]
solved = sorted(
    [(name, sqrt(x**2 + y**2) + d / 2) for (name, x, y, d) in splashes],
    reverse=True,
    key=lambda pair: pair[1],
)
assert notClose(solved[1], solved[0])
assert notClose(solved[2], solved[1])
assert notClose(solved[3], solved[2])

with open("00.in", "w") as inFile:
    inFile.write(f"{len(names)}\n")
    for name, x, y, d in splashes:
        inFile.write(f"{name}; ({x:2f}, {y:2f}); {d:2f}\n")

with open("00.out", "w") as outFile:
    for i in range(3):
        outFile.write(f"{solved[i][0]}\n")
