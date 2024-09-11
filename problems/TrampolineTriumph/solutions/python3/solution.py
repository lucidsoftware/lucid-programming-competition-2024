import math

def get_position(x, factor):
    return (6 - 2 * factor * math.sin(x / 2) 
              - 2 * factor * math.sin(x / 5) 
              - 2 * factor * math.sin(x / 7)) * (0.9 + (1 + math.sin(x * factor / 3)) / 20)

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

if __name__=="__main__":
    players_count = int(input())
    factors = list(map(float, input().split()))
    milestones_count = int(input())
    milestones = [list(map(float, input().split())) for _ in range(milestones_count)]
    scores = [0] * players_count
    for milestone in milestones:
        for i in range(players_count):
            scores[i] += get_score(milestone, factors[i])
    sorted_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    for i, score in sorted_scores:
        print(i + 1)
        print("{:.6f}".format(score))
