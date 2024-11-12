#!/usr/bin/env python3
from typing import List


def main(
    week_budget: int,
    num_gymnasts: int,
    gymnast_week_costs: List[int],
    gymnast_benefits: List[int],
) -> int:
    # Knapsack 0-1
    dp = [0] * (week_budget + 1)
    for i in range(num_gymnasts):
        for j in range(week_budget, gymnast_week_costs[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - gymnast_week_costs[i]] + gymnast_benefits[i])
    return dp[week_budget]
    # Algorithm written by Github Copilot


if __name__ == "__main__":
    answer = main(
        week_budget=int(input()),
        num_gymnasts=int(input()),
        gymnast_week_costs=[int(x) for x in input().split()],
        gymnast_benefits=[int(x) for x in input().split()],
    )
    print(answer)
