import random
from solutions import air_rifle


def generate_random_coordinates(num_points, range_limit):
    return [
        (
            random.randint(-range_limit, range_limit),
            random.randint(-range_limit, range_limit),
        )
        for _ in range(num_points)
    ]


def generate_test_case(num_competitors, num_bullets, max_distance):
    test_case = []
    test_case.append(f"{num_competitors} {num_bullets} {max_distance}")
    name_already_used = set()

    for _ in range(num_competitors):
        name = "".join(
            random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=5)
        )
        while name in name_already_used:
            name = "".join(
                random.choices(
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=5
                )
            )
        coordinates = generate_random_coordinates(num_bullets, 25)
        coordinates_str = " ".join(f"{x},{y}" for x, y in coordinates)
        test_case.append(f"{name} {coordinates_str}")

    return "\n".join(test_case)


def main():
    random.seed(42)  # For reproducibility

    for i in range(10, 11):
        solution = []
        # Example configurations
        num_competitors = random.randint(2, 10000)
        max_distance = random.randint(1, 10)

        # Generate the test case
        test_case = generate_test_case(num_competitors, 4 + i, max_distance)

        solution = air_rifle.test(test_case)
        # Write to a file
        with open(f"{i}.in", "w") as f:
            f.write(test_case)
        with open(f"{i}.out", "w") as f:
            winner = "\n".join(solution)
            f.write(winner)


if __name__ == "__main__":
    main()
