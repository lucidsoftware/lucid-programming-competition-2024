n, target = [float(x) for x in input().split()]
powers = [float(x) for x in input().split()]
multipliers = [float(x) for x in input().split()]


def permutations(nums):
    n = len(nums)
    if n == 1:
        return [nums]
    res = []
    for i in range(n):
        for perm in permutations(nums[:i] + nums[i+1:]):
            res.append([nums[i]] + perm)
    return res


combos = 0
power_permutations = permutations(powers)
for perm in power_permutations:
    score = sum([perm[i] * multipliers[i] for i in range(len(perm))])
    if score > target:
        combos += 1
print(combos)
