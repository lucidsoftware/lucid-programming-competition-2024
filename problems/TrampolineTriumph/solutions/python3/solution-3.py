from math import sin, cos, sqrt

def g(f):
    def gx(x):
        return (6 - 2 * f * sin(x / 2) - 2 * f * sin(x / 5) - 2 * f * sin(x / 7)) * (0.9 + (1 + sin(x * f / 3)) / 20)
    return gx


invphi = (sqrt(5) - 1) / 2  # 1 / phi


def gss(f, a, b):
    tolerance=1e-9
    while b - a > tolerance:
        c = b - (b - a) * invphi
        d = a + (b - a) * invphi
        if f(c) > f(d):
            b = d
        else:
            a = c

    return (b + a) / 2

n = int(input())
performance_factors = list(map(float, input().split()))
m = int(input())
milestones = [tuple(map(float, input().split())) for _ in range(m)]

player_fns = list(map(g, performance_factors))
scores = [0] * n

for (l, r) in milestones:
    mx = float('-inf')
    mx_player = None
    for i, fn in enumerate(player_fns):
        max_i = gss(fn, l, r)
        curr_max = fn(max_i)
        if curr_max > mx:
            mx = curr_max
            mx_player = i
    scores[mx_player] += 1

scores = [(s, -i) for i, s in enumerate(scores, start=1)]
for s, i in sorted(scores, reverse=True):
    print(f'{-i} {s}')
