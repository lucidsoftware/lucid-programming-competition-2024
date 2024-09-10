#!/usr/bin/env python3

from random import randint
from attr import dataclass
from depcache.generate_tests_lib import (
    generate_many_test_cases,
)
from depcache.randomness import rand_with_log_density
import depcache.main as solution_finder


@dataclass
class HeartfeltTestCaseInput:
    num_gymnasts: int
    gymnasts_week_costs: list[int]
    gymnasts_benefits: list[int]
    week_capacity: int

    def __str__(self):
        return f"Scheduling {self.num_gymnasts} gymnasts with a budget of {self.week_capacity}. Costs were up to {max(self.gymnasts_week_costs)} and benefits were up to {max(self.gymnasts_benefits)}"

    def write(self, f):
        f.write(f"{self.week_capacity}\n")
        f.write(f"{self.num_gymnasts}\n")
        f.write(" ".join(map(str, self.gymnasts_week_costs)) + "\n")
        f.write(" ".join(map(str, self.gymnasts_benefits)) + "\n")


@dataclass
class HeartfeltTestCaseOutput:
    solution: int

    def __str__(self):
        return f"{self.solution}"

    def write(self, f):
        f.write(f"{self.solution}\n")


def random_heartfelt_test_case_input() -> HeartfeltTestCaseInput:
    num_gymnasts = rand_with_log_density(4)
    max_week_cost = rand_with_log_density(5)
    max_profit = rand_with_log_density(5)
    gymnasts_benefits = [randint(1, max_profit) for _ in range(num_gymnasts)]
    return HeartfeltTestCaseInput(
        num_gymnasts=num_gymnasts,
        gymnasts_week_costs=[randint(1, max_week_cost) for _ in range(num_gymnasts)],
        gymnasts_benefits=gymnasts_benefits,
        week_capacity=randint(1, sum(gymnasts_benefits)),
    )


def verify_heartfelt_test_case(
    input: HeartfeltTestCaseInput, solution: HeartfeltTestCaseOutput
) -> None:
    if solution.solution >= sum(input.gymnasts_benefits):
        print(
            f"Retrying test case with a solution of {solution} and a sum of benefits of {sum(input.gymnasts_benefits)}."
        )
        raise Exception("Solution is too high.")


def find_solution(input: HeartfeltTestCaseInput) -> HeartfeltTestCaseOutput:
    return HeartfeltTestCaseOutput(
        solution_finder.main(
            input.week_capacity,
            input.num_gymnasts,
            input.gymnasts_week_costs,
            input.gymnasts_benefits,
        )
    )


if __name__ == "__main__":
    generate_many_test_cases(
        test_prefix=input("test_path: "),
        the_range=range(
            *[int(x) for x in input("test_path index range(**): ").split()]
        ),
        random_test_case_input=random_heartfelt_test_case_input,
        find_solution=find_solution,
        verify_solution=verify_heartfelt_test_case,
    )
