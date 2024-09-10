from itertools import permutations

pulling_powers = [float(i) for i in input().split()]
multipliers = [float(i) for i in input().split()]
opposition = eval(input())

count = 0
orders = permutations(pulling_powers, len(pulling_powers))
for order in orders:
    my_team = sum([order[i] * multipliers[i] for i in range(len(order))])
    if my_team > opposition:
        count += 1
print(count)
