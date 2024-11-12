# This solution does not work

import sys

sys.setrecursionlimit(1000000)

S = int(input())
A = int(input())
sessionLengths = [int(ea) for ea in input().split(' ')]
sessionCosts = [int(ea) for ea in input().split(' ')]

memo = {}
def maxBenefitFromRemainingSessions(i, timeLeft):
    key = (i, timeLeft)
    if key not in memo:
        if timeLeft < 0:
            res = -1 * float('inf')
        elif i >= A:
            res = 0
        elif timeLeft == 0:
            res = 0
        else:
            # Check both taking and skipping current choice
            skipBenefit = maxBenefitFromRemainingSessions(i+1, timeLeft)
            takeBenefit = maxBenefitFromRemainingSessions(i+1, timeLeft - sessionLengths[i])
            takeBenefit += sessionCosts[i]
            if takeBenefit > skipBenefit:
                res = takeBenefit
            else:
                res = skipBenefit
        memo[key] = res
    return memo[key]

print(maxBenefitFromRemainingSessions(0, S))
