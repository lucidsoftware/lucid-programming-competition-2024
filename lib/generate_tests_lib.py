import multiprocessing
import sys
import time
from typing import Callable

from attr import dataclass


@dataclass
class TestCase[Input, Output]:
    input: Input
    solution: Output
    time_to_solve: float

    def report(self, where: str = ""):
        print(
            f"- {where} Took {self.time_to_solve:0.3} seconds to solve: {self.input}. Solution: {self.solution}",
            file=sys.stderr,
        )

    def write_at(self, test_path: str):
        with open(f"{test_path}.in", "w") as f:
            self.input.write(f)  # type: ignore
        with open(f"{test_path}.out", "w") as f:
            self.solution.write(f)  # type: ignore


def create_one_test_case[Input, Output](
    random_test_case_input: Callable[..., Input],
    find_solution: Callable[[Input], Output],
    verify_solution: Callable[[Input, Output], None],
    max_solve_seconds: float = 1,
) -> TestCase[Input, Output]:
    """
    Generates a test case with the given parameters and writes it to the given path.

    Verifies that the solution is correct and that it runs in a reasonable amount of time.
    """
    input_obj = random_test_case_input()
    # Time it
    start_time = time.time()
    with multiprocessing.Pool(processes=1) as pool:
        try:
            async_result = pool.apply_async(
                find_solution,
                (input_obj,),
            )
            solution = async_result.get(timeout=max_solve_seconds)
        except multiprocessing.TimeoutError:
            print(f"Stopped generating test case that was taking too long: {input_obj}")
            raise Exception("Solution took too long.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    verify_solution(input_obj, solution)

    return TestCase(
        input=input_obj,
        solution=solution,
        time_to_solve=elapsed_time,
    )


def generate_many_test_cases[Input, Output](
    test_prefix: str,
    the_range: range,
    random_test_case_input: Callable[[], Input],
    find_solution: Callable[[Input], Output],
    verify_solution: Callable[[Input, Output], None],
    max_solve_seconds: float = 1,
):
    cases = []
    for i in the_range:
        while True:
            try:
                the_case = create_one_test_case(
                    random_test_case_input=random_test_case_input,
                    find_solution=find_solution,
                    verify_solution=verify_solution,
                    max_solve_seconds=max_solve_seconds,
                )
                the_case.report()
                cases.append(the_case)
                break
            except Exception:
                pass
    print()
    print("Sorting test cases by time to solve.")
    print()
    cases.sort(key=lambda x: x.time_to_solve)
    for i, the_case in zip(the_range, cases):
        test_path = f"{test_prefix}{i}"
        the_case.report(test_path)
        the_case.write_at(test_path)
