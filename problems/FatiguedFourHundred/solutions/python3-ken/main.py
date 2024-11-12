#!/usr/bin/env python3


from dataclasses import dataclass
from typing import Tuple

# This is the penalty applied only on a per-leg basis - the more effort, the faster you go.
effort_time_penalties = {
    75: 1.160,
    80: 1.125,
    85: 1.088,
    90: 1.055,
    95: 1.026,
    100: 1.00,
}

# This is the fatigue penalty the applies on later legs from applying effort on this leg.
progressive_fatigue_penalties = {
    75: 1.015,
    80: 1.022,
    85: 1.032,
    90: 1.045,
    95: 1.060,
    100: 1.10,
}


class EffortLevel:

    def __init__(self, level: int):
        self.level = level

        # Very small optimization: cache the penalty lookups
        self.time_penalty = effort_time_penalties[self.level]
        self.progressive_penalty = progressive_fatigue_penalties[self.level]

    def __str__(self) -> str:
        return f"{self.level}"

    def __repr__(self) -> str:
        return str(self)


class EffortLevelTuple:

    @staticmethod
    def iter_all_possible():
        import itertools

        for efforts in itertools.product(effort_time_penalties.keys(), repeat=3):
            yield EffortLevelTuple(efforts + (100,))

    def __init__(self, efforts: Tuple[int]):
        self.efforts: Tuple[EffortLevel] = tuple(
            [EffortLevel(level) for level in efforts]
        )

        # Precomputing the string form saves about 2% of the total execution time, but only as long as you
        #  also cache all possible tuple objects as well and don't recreate them in a loop.
        self.effort_str = " ".join(str(effort) for effort in self.efforts)

        # Precomputing these saves enough floating point multiplications to save
        #  about 25% of the total execution time
        self.effective_time_penalties = tuple(self._precompute_effective_efforts())

    def __str__(self) -> str:
        return self.effort_str

    def _precompute_effective_efforts(self):
        progressive_fatigue = 1.00
        for effort in self.efforts:
            yield effort.time_penalty * progressive_fatigue
            progressive_fatigue *= effort.progressive_penalty

    def compute_total_time(self, times: Tuple[int]) -> float:
        total_time = 0.0
        for penalty, time in zip(self.effective_time_penalties, times):
            total_time += penalty * time
        return total_time


# Precomputing these seems to be essential. In testing, failure to
#  precompute the cartesian product could make things 6x slower.
precomputed_possible_effort_levels = tuple(EffortLevelTuple.iter_all_possible())


class Swimmer:

    def __init__(
        self, butterfly: float, backstroke: float, breaststroke: float, freestyle: float
    ) -> None:
        self.times = [butterfly, backstroke, breaststroke, freestyle]

    def optimal_effort_level(self):
        fastest_time = float("inf")
        effort_levels = None

        for effort_tuple in precomputed_possible_effort_levels:
            attempt_time = effort_tuple.compute_total_time(self.times)

            if attempt_time < fastest_time:
                fastest_time = attempt_time
                effort_levels = effort_tuple
            elif attempt_time == fastest_time:
                raise AssertionError("Non unique solution situation detected")

        return effort_levels, fastest_time


def format_swimmer_results(effort_levels: EffortLevelTuple, total_time: float) -> str:
    return "{} {:.1f}".format(effort_levels, total_time)


def main():
    num_swimmers = int(input())
    for _ in range(num_swimmers):
        swimmer = Swimmer(*[float(best_time) for best_time in input().split()])
        result = swimmer.optimal_effort_level()
        print(format_swimmer_results(*result))


if __name__ == "__main__":
    main()
