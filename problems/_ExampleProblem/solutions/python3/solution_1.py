n = eval(input())

# Key: name, Value: wateringHole
dinosaurs = {}
# Key: wateringHole, Value: nameList
wateringHoles = {}
for i in range(n):
    log = input().split()
    name, hole = log[0], eval(log[1])
    if hole == 0:
        oldHole = dinosaurs[name]
        dinosaurs[name] = 0
        wateringHoles[oldHole].remove(name)
    else:
        if name in dinosaurs:
                oldHole = dinosaurs[name]
                wateringHoles[oldHole].remove(name)
        if hole in wateringHoles:
            wateringHoles[hole].append(name)
        else:
            wateringHoles[hole] = [name]
        dinosaurs[name] = hole

for hole in sorted(wateringHoles.keys()):
    nameList = wateringHoles[hole]
    if len(nameList) == 0:
        print(f'{hole} n/a')
    else:
        print(f'{hole} {" ".join(sorted(wateringHoles[hole]))}')