import itertools

n, power_to_beat = map(eval, input().split())
powers = [float(ea) for ea in input().split(" ")]
multipliers = [float(ea) for ea in input().split(" ")]

successful_combinations = 0
for lineup in list(itertools.permutations(powers, len(powers))):
    if sum([lineup[i] * multipliers[i] for i in range(len(powers))]) > power_to_beat:
        successful_combinations += 1

print(successful_combinations)