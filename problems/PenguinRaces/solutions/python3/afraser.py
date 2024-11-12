n = int(input())
penguins = []
for i in range(n):
    line = input().split(' - ')
    penguins.append((line[0], int(line[1])))

penguins.sort(key=lambda tup: tup[1])


print("First: " + str(penguins[0][0]))
print("Second: " + str(penguins[1][0]))
print("Third: " + str(penguins[2][0]))