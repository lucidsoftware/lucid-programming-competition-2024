from collections import defaultdict

N = int(input())

wateringHoles = defaultdict(set)
dinoLocation = {}

for n in range(N):
    log = input().split(' ')
    name = log[0]
    hole = int(log[1])
    if name in dinoLocation: wateringHoles[dinoLocation[name]].remove(name)
    if hole > 0:
        wateringHoles[hole].add(name)
    dinoLocation[name] = hole

for hole in sorted(wateringHoles.keys()):
    dinos = wateringHoles[hole]
    if (len(dinos) == 0):
        print(f'{hole} n/a')
    else:
        print(f'{hole} {" ".join(sorted(dinos))}')
