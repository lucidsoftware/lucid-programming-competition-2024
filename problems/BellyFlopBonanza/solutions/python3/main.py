from collections import namedtuple
from math import sqrt
from re import match

Splash = namedtuple("Splash", ["name", "x", "y", "d"])


def parse(line):
    result = match(r"^(.+); \((.+), (.+)\); (.+)$", line)
    assert result is not None
    (name, x, y, d) = result.group(1, 2, 3, 4)
    return Splash(name, float(x), float(y), float(d))


def score(splash):
    return sqrt(splash.x**2 + splash.y**2) + splash.d / 2


n = int(input())
splashes = [parse(input()) for _ in range(n)]
splashes.sort(reverse=True, key=score)

for i in range(3):
    print(splashes[i].name)
