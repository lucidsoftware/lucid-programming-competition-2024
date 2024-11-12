BASE_EFFORT = 75
STROKES = 4
EFFORTS = [
    [0.160, 0.015],
    [0.125, 0.022],
    [0.088, 0.032],
    [0.055, 0.045],
    [0.026, 0.060],
    [0.000, 0.100],
]
count = len(EFFORTS)

get_effort = lambda i: BASE_EFFORT + i * 5

def get_penalties(stroke_effort_indexes):
    penalties = [[] for _ in range(STROKES)]
    for i in range(STROKES):
        effort_index = stroke_effort_indexes[i]
        penalties[i].append(EFFORTS[effort_index][0])
        for j in range(i + 1, STROKES):
            penalties[j].append(EFFORTS[effort_index][1])
            
    return penalties

def get_total_penalties(penalties):
    total_penalties = [1 for _ in range(STROKES)]
    for i in range(STROKES):
        for penalty in penalties[i]:
            total_penalties[i] *= 1 + penalty

    return total_penalties

def get_combinations():
    for i in range(count):
        for j in range(count):
            for k in range(count):
                yield [i, j, k, count - 1]

def pretty_print_combination(combination):
    for i in range(STROKES):
        print(get_effort(combination[i]), end=" ")

def solve(stroke_timings):
    minimum_time = float('inf')
    minimum_combination = None
    for combination in get_combinations():
        penalties = get_penalties(combination)
        total_penalties = get_total_penalties(penalties)
        stroke_timings_after_penalties = [stroke_timings[i] * total_penalties[i] for i in range(STROKES)]
        total_time = sum(stroke_timings_after_penalties)
        if total_time < minimum_time:
            minimum_time = total_time
            minimum_combination = combination

    pretty_print_combination(minimum_combination)
    print('{:.1f}'.format(minimum_time))

swimmers = int(input())
for _ in range(swimmers):
    stroke_timings = list(map(float, input().split()))
    solve(stroke_timings)
    