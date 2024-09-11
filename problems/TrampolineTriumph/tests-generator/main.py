import random, math, sys

def printerr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_position(x, factor):
    return (6 - 2 * factor * math.sin(x / 2) 
              - 2 * factor * math.sin(x / 5) 
              - 2 * factor * math.sin(x / 7)) * (0.9 + (1 + math.sin(x * factor / 3)) / 20)

def is_valid(milestone, factors):
    step = 0.1
    left = milestone[0] - step
    right = milestone[1] + step

    for factor in factors:
        increasing = None
        first_switch = None
        previous_value = get_position(left, factor)
        
        x = left + step
        while x <= right:
            current_value = get_position(x, factor)
            if increasing is None:
                if current_value < previous_value:
                    printerr("{:.2f} ({:.2f}) {:.2f}".format(left, x, milestone[1]))
                    return False
            else:
                if increasing:
                    if current_value < previous_value:
                        increasing = False
                        first_switch = (x, current_value)
                else:
                    if current_value > previous_value:
                        second_switch = (x, current_value)
                        printerr("{:.2f} ({:.2f}) ({:.2f}) {:.2f}".format(milestone[0], first_switch[0], second_switch[0], milestone[1]))
                        return False

            increasing = current_value > previous_value
            previous_value = current_value
            x += step

    return True

def get_local_maxima(l, r, factor):
    while r - l > 1e-9:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if get_position(m1, factor) > get_position(m2, factor):
            r = m2
        else:
            l = m1
    return l

def get_score(milestone, factor):
    local_maxima = get_local_maxima(milestone[0], milestone[1], factor)
    local_maxima_value = get_position(local_maxima, factor)
    return local_maxima_value if local_maxima_value >= milestone[2] else 0

def get_victories(milestones, factors):
    players_count = len(factors)
    victories = [0] * (players_count + 1)
    for milestone in milestones:
        max_score = None
        winner = None
        for i in range(players_count):
            score = get_score(milestone, factors[i])
            if max_score is None:
                if score > 0:
                    max_score = score
                    winner = i
            elif score > max_score:
                max_score = score
                winner = i
        if winner is not None:
            victories[winner] += 1
        else:
            victories[players_count] += 1
    return victories

def generate_test_case(max_value):
    players_count = random.randint(2, 10)
    factors = [random.uniform(0.76, 0.99) for _ in range(players_count)]
    milestones_count = max(2, random.randint(max_value // 10, max_value))
    minimum_range_per_milestone = 50
    minimum_range = minimum_range_per_milestone * milestones_count
    milestone_search_range = max(minimum_range, max_value - 1)

    milestones = []
    milestone_locations = set()
    while len(milestones) < milestones_count:
        left = random.uniform(1, milestone_search_range)
        right = left + random.uniform(5, 15)
        height = random.uniform(2, 10)
        milestone = [left, right, height]
        if is_valid(milestone, factors):
            milestone_location = get_local_maxima(left, right, factors[0])
            if milestone_location not in milestone_locations:
                milestone_locations.add(milestone_location)
                milestones.append(milestone)
            else:
                printerr("Duplicate milestone location", milestone, milestone_location)

    scores = [[round(get_score(milestone, factor), 1) for milestone in milestones] for factor in factors]
    victories = get_victories(milestones, factors)
    actual_victories = victories[:players_count]
    # if sum(1 for victory in actual_victories if victory > 0) < 2:
    if not all(victories):
        printerr("Invalid victories distribution", victories, scores)
        return None
    else:
        printerr(victories)
        printerr(scores)
        return players_count, factors, milestones_count, milestones

def keep_generating_test_case(max_value):
    c = 100
    while True:
        test_case = generate_test_case(max_value)
        if test_case is not None:
            return test_case
        c -= 1
        if c == 0:
            printerr("Failed to generate test case")
            sys.exit(1)

def format_test_case(test_case):
    players_count, factors, milestones_count, milestones = test_case
    print(players_count)
    print(' '.join(["{:.6f}".format(factor) for factor in factors]))
    print(milestones_count)
    for milestone in milestones:
        print(' '.join(["{:.6f}".format(value) for value in milestone]))

# sample cases manually generated- 1 to 3
# test cases- 4 to 6
# format_test_case(keep_generating_test_case(10))
# test cases- 7 to 9
# format_test_case(keep_generating_test_case(100))
# # test cases- 10 to 12
format_test_case(keep_generating_test_case(10000))
