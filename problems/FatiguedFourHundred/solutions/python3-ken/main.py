#!/usr/bin/env python3


from dataclasses import dataclass
from typing import Tuple


effort_penalties = {
    75: 1.160,
    80: 1.125,
    85: 1.088,
    90: 1.055,
    95: 1.026,
    100: 1.00,
}

progressive_penalties = {
    75: 1.015,
    80: 1.025,
    85: 1.035,
    90: 1.045,
    95: 1.060,
    100: 1.10,
}

class Swimmer:

    def __init__(self, butterfly: float, backstroke: float, breaststroke: float, freestyle: float) -> None:
        self.times = [butterfly, backstroke, breaststroke, freestyle]

    def all_possible_effort_permutations(self):
        import itertools
        for effort_levels in itertools.permutations(effort_penalties.keys(), 3):
            # We always exert 100% effort in the last leg (freestyle) since the
            #  progressive penalty will not matter after this.
            yield effort_levels + (100,)

    def compute_total_time(self, effort_level_per_stroke: Tuple[int]) -> float:
        progressive_fatigue = 1.00
        total_time = 0.00
        for i, time in enumerate(self.times):
            effort_level = effort_level_per_stroke[i]

            # A common mistake is adding the fatigue penalties instead of multiplying
            total_time += time * effort_penalties[effort_level] * progressive_fatigue

            # This step must come last since the progressive fatigue does not apply
            # to the current leg of the race (this could be a common mistake)
            progressive_fatigue *= progressive_penalties[effort_level]
        return total_time

    def optimal_effort_level(self):
        fastest_time = float('inf')
        effort_levels = None

        for effort_permutation in self.all_possible_effort_permutations():
            attempt_time = self.compute_total_time(effort_permutation)
            if attempt_time < fastest_time:
                fastest_time = attempt_time
                effort_levels = effort_permutation
            elif attempt_time == fastest_time:
                raise AssertionError("Non unique solution situation detected")

        return effort_levels, fastest_time

def format_swimmer_results(effort_levels: Tuple[int], total_time: float) -> str:
    total_time_str = " {:.2f}".format(round(total_time, 2))
    return " ".join(map(str, effort_levels)) + total_time_str

def main():
    num_swimmers = int(input())
    for _ in range(num_swimmers):
        swimmer = Swimmer(*[float(best_time) for best_time in input().split()])
        result = swimmer.optimal_effort_level()
        print(format_swimmer_results(*result))



if __name__ == "__main__":
    main()
