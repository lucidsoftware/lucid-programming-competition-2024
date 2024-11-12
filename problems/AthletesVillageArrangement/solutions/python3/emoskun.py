n = int(input())
forward = dict([(input(), set(input().split())) for _ in range(n)])

mutual = dict(
    [(k, set(filter(lambda x: k in forward[x], v))) for k, v in forward.items()]
)
start = next(iter(forward))


def hamiltonianCycle(path):
    last = path[-1]

    if len(path) == n:
        return start in mutual[last]

    for neighbor in mutual[last]:
        if neighbor not in path:
            copy = path.copy()
            copy.append(neighbor)
            if hamiltonianCycle(copy):
                return True

    return False


print(str(hamiltonianCycle([start])).lower())
