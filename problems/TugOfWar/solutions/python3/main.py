from itertools import permutations

n, opposition = map(eval, input().split())
pulling_powers = [float(i) for i in input().split()]
multipliers = [float(i) for i in input().split()]

count = 0
orders = permutations(pulling_powers, n)
for order in orders:
    my_team = sum([order[i] * multipliers[i] for i in range(len(order))])
    if my_team > opposition:
        count += 1
print(count)