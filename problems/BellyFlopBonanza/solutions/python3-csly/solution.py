from math import sqrt
from re import fullmatch

def get_distance(x, y, diameter) -> float:
    return sqrt(x**2 + y**2) + diameter / 2

if __name__=="__main__":
    # Parse input and compute the distance for each athlete
    num_athletes = int(input())
    athletes = []
    for _ in range(num_athletes):
        raw = fullmatch(r"^(.+); \((.+), (.+)\); (.+)$", input())
        name = raw[1]
        x = float(raw[2])
        y = float(raw[3])
        diameter = float(raw[4])
        athletes.append((name, get_distance(x, y, diameter)))
    sorted_athletes = sorted(athletes, key=lambda x: x[1], reverse=True)
    for i in range(3):
        print(sorted_athletes[i][0])