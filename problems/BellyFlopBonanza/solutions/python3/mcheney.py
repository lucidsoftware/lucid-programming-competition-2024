import math

N = int(input())

namesByDistance = []  # [(name, distance)]
for n in range(N):
    line = input().split('; ')
    name = line[0]
    [x, y] = [float(ea) for ea in line[1][1:-1].split(', ')]
    d = float(line[2])
    distance = math.sqrt(x ** 2 + y ** 2) + (d / 2)
    namesByDistance.append([name, distance])

namesByDistance.sort(key=lambda x: x[1], reverse=True)
print(namesByDistance[0][0])
print(namesByDistance[1][0])
print(namesByDistance[2][0])
