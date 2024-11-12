import sys
import math

data = sys.stdin.readlines()
n_players = int(data[0])
factors = [float(x) for x in data[1].split()]
n_milestones = int(data[2])
milestones = []

def g(x, f):
  return (6 - 2 * f * math.sin(x / 2) - 2 * f * math.sin(x / 5) - 2 * f * math.sin(x / 7)) * (0.9 + (1 + math.sin(x * f / 3)) / 20)

def dg(x, f):
  # return (6 - 2 * f * math.sin(x / 2) - 2 * f * math.sin(x / 5) - 2 * f * math.sin(x / 7)) * (0.9 + (1 + math.sin(x * f / 3)) / 20)
  return - 1 / 10 * f * (math.cos(x / 2) / 2 + math.cos(x / 5) / 5 + math.cos(x / 7) / 7) * (math.sin(f * x / 3) + 19) - 1 / 30 * f * ( f * (math.sin(x / 2) + math.sin(x / 5) + math.sin(x / 7)) - 3) * math.cos(f * x / 3)

# def find_root(f, x_min, x_max):
#   root_result = root_scalar(g, args=(f,), bracket=[x_min, x_max], method='bisect')

def find_root(f, x_min, x_max):
    tol = 1e-9
    if dg(x_min, f) * dg(x_max, f) >= 0:
        # print(dg(x_min, f), dg(x_max, f))
        # print('uh oh')
        return x_min if g(x_min, f) > g(x_max, f) else x_max

    while True:
        x_mid = (x_min + x_max) / 2.0
        g_mid = dg(x_mid, f)

        if abs(g_mid) < tol:
            return x_mid
        if dg(x_min, f) * g_mid < 0:
            x_max = x_mid
        else:
            x_min = x_mid

for i in range(3,3+n_milestones):
  items = data[i].split()
  x = float(items[0])
  y = float(items[1])
  milestones.append((x, y))

winners = {spot: 0 for spot in range(n_players)}
for i in range(n_milestones):
  max_n = -1
  max_val = 0
  for n in range(n_players):
    root = find_root(factors[n], milestones[i][0], milestones[i][1])
    val = g(root, factors[n])
    if val > max_val:
      max_val = val
      max_n = n
  winners[max_n] += 1

res = sorted( ((v,-k) for k,v in winners.items()), reverse=True)
for (wins, num) in res:
    print(-num+1, wins)
# print(res)
