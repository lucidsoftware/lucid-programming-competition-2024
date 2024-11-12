def solve(graph, seating, used):
    if (len(seating) == len(graph)):
        start = seating[0]
        end = seating[-1]
        return end in graph[start]

    curr = seating[-1]
    result = []
    for person in graph[curr]:
        if person not in used:
            seating.append(person)
            used.add(person)
            if(solve(graph, seating, used)):
                return True
            seating.pop()
            used.remove(person)
    
    return False

N = int(input())

graph = {}
for i in range(N):
    name = input()
    graph[name] = set()
    for dep in input().split():
        graph[name].add(dep)

for start in graph:
    thingsToRemove = set()
    for end in graph[start]:
        if start not in graph[end]:
            thingsToRemove.add(end)
    
    for el in thingsToRemove:
        graph[start].remove(el)

start = list(graph.keys())[0]
print("true" if solve(graph, [start], {start}) else "false")