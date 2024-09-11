from math import sqrt
from random import choices, randint, uniform
from string import ascii_letters


def makeName():
    return "".join(choices(ascii_letters, k=randint(5, 10)))


def makeDisplacement():
    return uniform(-10, 10)


def makeDistance():
    return abs(makeDisplacement())


def notClose(left, right):
    return abs(left[1] - right[1]) > 0.1


for test in range(1, 20):
    n = randint(5, 5 + test**3 * 3)
    splashes = []
    solved = []
    acceptable = False

    while not acceptable:
        splashes = [
            (makeName(), makeDisplacement(), makeDisplacement(), makeDistance())
            for _ in range(n)
        ]

        solved = sorted(
            [(name, sqrt(x**2 + y**2) + d / 2) for (name, x, y, d) in splashes],
            reverse=True,
            key=lambda pair: pair[1],
        )

        acceptable = (
            len(set([splash[0] for splash in splashes])) == len(splashes)
            and notClose(solved[1], solved[0])
            and notClose(solved[2], solved[1])
            and notClose(solved[3], solved[2])
        )

    with open(f"{test:02}.in", "w") as inFile:
        inFile.write(f"{n}\n")
        for name, x, y, d in splashes:
            inFile.write(f"{name}; ({x:2f}, {y:2f}); {d:2f}\n")

    with open(f"{test:02}.out", "w") as outFile:
        for i in range(3):
            outFile.write(f"{solved[i][0]}\n")
