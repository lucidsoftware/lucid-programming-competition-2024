n = eval(input())
countryPreferences: dict[str, set[str]] = dict()

for _ in range(n):
    countryName = input()
    preferenceList = input().split()
    countryPreferences[countryName] = set(preferenceList)


def dfs(path: list[str], curr: str, visited: set[str]) -> bool:
    # if path is complete and forms a cycle
    if len(path) == len(countryPreferences):
        return path[0] in countryPreferences[curr]  # check if it forms a ring

    for neighbor in countryPreferences[curr]:
        if neighbor not in visited and curr in countryPreferences[neighbor]:
            visited.add(neighbor)
            path.append(neighbor)
            if dfs(path, neighbor, visited):
                return True
            visited.remove(neighbor)
            path.pop()  # backtrack

    return False


# start DFS from the first country in the list
startCountry = next(iter(countryPreferences))
print('true' if dfs([startCountry], startCountry, {startCountry}) else 'false')
