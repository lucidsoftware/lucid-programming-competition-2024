import math

def get_position(x, factor):
    return (6 - 2 * factor * math.sin(x / 2) 
              - 2 * factor * math.sin(x / 5) 
              - 2 * factor * math.sin(x / 7)) * (0.9 + (1 + math.sin(x * factor / 3)) / 20)

def get_local_maxima(l, r, factor):
    while r - l > 1e-9: # 1e-3 is the lowest precision that works
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        # m2 = l + 2 * ((r - l) / 3) # alternative
        if get_position(m1, factor) > get_position(m2, factor):
            r = m2
        else:
            l = m1
    return l
    # return (l + r) / 2 # alternative

def get_jump_distance(milestone, factor):
    local_maxima = get_local_maxima(milestone[0], milestone[1], factor)
    return get_position(local_maxima, factor)

def get_scores(milestones, factors):
    players_count = len(factors)
    scores = [0] * players_count
    for milestone in milestones:
        max_jump_distance = None
        winner = None
        for i in range(players_count):
            jump_distance = get_jump_distance(milestone, factors[i])
            if max_jump_distance is None or jump_distance > max_jump_distance:
                max_jump_distance = jump_distance
                winner = i
            elif jump_distance == max_jump_distance:
                print("Error: multiple winners")
        scores[winner] += 1
    return scores

if __name__=="__main__":
    players_count = int(input())
    factors = list(map(float, input().split()))
    milestones_count = int(input())
    milestones = [list(map(float, input().split())) for _ in range(milestones_count)]
    scores = get_scores(milestones, factors)
    sorted_scores = sorted(enumerate(scores), key=lambda x: (-x[1], x[0]))
    for i, score in sorted_scores:
        print(i + 1, score)
