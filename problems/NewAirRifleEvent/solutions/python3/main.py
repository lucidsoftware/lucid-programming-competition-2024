import sys


def parse_input():
    input = sys.stdin.read().strip().splitlines()
    first_line = input[0].split()
    A = int(first_line[0])
    N = int(first_line[1])
    M = int(first_line[2])

    competitors = []
    for line in input[1:]:
        parts = line.split()
        name = parts[0]
        coordinates = [tuple(map(int, coord.split(","))) for coord in parts[1:]]
        competitors.append((name, coordinates))

    return A, N, M, competitors


def distance_from_origin(final_coordinates):
    return (final_coordinates[0] ** 2 + final_coordinates[1] ** 2) ** 0.5


def has_duplicates(points):
    return len(set(points)) != len(points)


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def compute_convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def main():
    A, N, M, competitor_results = parse_input()
    winner = []
    for name, coordinates in competitor_results:
        last_shot = coordinates[-1]
        # Calculate the distance from the target center for the last shot first
        if distance_from_origin(last_shot) > M:
            # If the last shot is not within the distance to bullseye, the competitor is disqualified
            continue

        # If there are points that are the same, the competitor is disqualified
        if has_duplicates(coordinates):
            continue

        # Calculate if N-1 shots are the convex hull
        # If we can compute a convex hull that doesn't use the last bullet, that means the last bullet is within the convex hull.
        hull_points = compute_convex_hull(coordinates)
        if (len(hull_points) == N - 1) and (last_shot not in hull_points):
            print(name)


if __name__ == "__main__":
    main()
