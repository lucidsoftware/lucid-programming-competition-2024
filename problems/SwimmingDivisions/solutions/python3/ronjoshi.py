import sys

sys.setrecursionlimit(100000)

n = int(input())
names = []

name_to_idx = {}
for i in range(n):
    name = input()
    names.append(name)
    name_to_idx[name] = i

# link[i] is the person that i "points to", i.e. they have won
# against i. If we want to look at the winner of i's league,
# then we use the find_set disjoint set algorithm to basically calculate
# link[link[link[...link[i]]]]]] to get the winner.
link = []
for i in range(n):
    link.append(i)

# finds top-ranked player in x's league
def find_set(x):
    if x != link[x]:
        link[x] = find_set(link[x])
    return link[x]

# y defeats x in a competition
def unite(x, y):
    link[find_set(x)] = y

n_done = 0

while True:
    line = input().split()
    if line[0] == "COMPETITION":
        n_compete = int(line[1])

        winner = -1
        for i in range(n_compete):
            name = input()
            idx = name_to_idx[name]
            if winner == -1:
                # A little trickery is needed to properly set the
                # winners! This way, the old winner is guaranteed to point to
                # the new winner. And the new winner obviously points to themselves.
                winner = idx
                old_winner = find_set(winner)
                link[winner] = winner
                unite(old_winner, winner)
            else:
                unite(idx, winner)

    elif line[0] == "REQUEST":
        idx = name_to_idx[line[1]]
        print(names[find_set(idx)])

    if line[0] == "END":
        break
