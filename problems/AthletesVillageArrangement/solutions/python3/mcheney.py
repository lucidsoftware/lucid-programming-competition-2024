# Build a graph, where countries are nodes and preferences are edges
# Use backtracking to discover path that hits every node exactly once

DEBUG = False

N = int(input())
oneDirectionalPreferences = {}
for n in range(N):
    country = input()
    preferences = input().split(' ')
    oneDirectionalPreferences[country] = set(preferences)
twoDirectionalPreferences = {}
for country in oneDirectionalPreferences.keys():
    twoDirectionalPreferences[country] = []
    for otherCountry in oneDirectionalPreferences[country]:
        if country in oneDirectionalPreferences[otherCountry]:
            twoDirectionalPreferences[country].append(otherCountry)

visited = set()
path = []
firstCountry = next(iter(twoDirectionalPreferences))
def findPath(cur):
    if cur == firstCountry and len(visited) == len(twoDirectionalPreferences):
        if DEBUG: print(*path)
        return True
    if cur in visited:
        return False
    path.append(cur)
    visited.add(cur)
    for edge in twoDirectionalPreferences[cur]:
        if (findPath(edge)):
            return True
    visited.remove(cur)
    path.pop(-1)
    return False

print("true" if findPath(firstCountry) else "false")
