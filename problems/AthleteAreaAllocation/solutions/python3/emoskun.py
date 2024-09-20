from dataclasses import dataclass
from math import sqrt


@dataclass
class Flag:
    x: int
    y: int

    @classmethod
    def parse(cls, serialized):
        x, y = serialized.split()
        return cls(int(x), int(y))

    def dx(self, other):
        return abs(self.x - other.x)
    
    def dy(self, other):
        return abs(self.y - other.y)

    def dist(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


n = int(input())
flags = [Flag.parse(input()) for _ in range(n)]
flags.sort(key=lambda flag: flag.x)

nearest = float("inf")
for i in range(n):
    j = i + 1
    while j < n and flags[i].dx(flags[j]) < nearest:
        if flags[i].dy(flags[j]) < nearest:
            nearest = min(nearest, flags[i].dist(flags[j]))
        j += 1
print(round(nearest, 3))
