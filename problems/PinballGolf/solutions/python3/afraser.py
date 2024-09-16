import math
import sys

def linearSearch(arr, number):
    if number > arr[len(arr) - 1][0]:
        return -1
    
    for i in range(len(arr) - 2, -1, -1):
        if number > arr[i][0]:
            return arr[i+1][1]
    
    return arr[0][1]


def topoSort(graph):
    visited = set()
    topoList = []

    for i in graph:
        dfs(i, graph, visited, topoList)
    
    return topoList

def dfs(vertex, graph, visited, topoList):
    if vertex in visited:
        return
    
    visited.add(vertex)

    for adj in graph[vertex]:
        dfs(adj, graph, visited, topoList)
    
    topoList.append(vertex)

sys.setrecursionlimit(100000)

[N, L] = map(lambda x: int(x), input().split(" "))

coords = {}
positionGraph = {}
flipperPositions = {}

for i in range(N):
    [x, y, k] = map(lambda x: int(x), input().split(" "))
    directions = list(map(lambda x: int(x), input().split(" ")))

    if x not in coords:
        coords[x] = []
    coords[x].append((y, i))

    flipperPositions[i] = (x, y)
    positionGraph[i] = directions

if 0 not in coords:
    coords[0] = []

coords[0].append((L, N))

for coord in coords:
    coords[coord].sort(key=lambda tup: tup[0])

graph = {}
graph[-1] = []
graph[N] = []

for i in positionGraph:
    graph[i] = []
    for dir in positionGraph[i]:
        [x, y] = flipperPositions[i]
        newX = x + dir
        adj = -1
        if newX in coords:
            adj = linearSearch(coords[newX], y)
        
        if adj == -1 and newX == 0:
            adj = N
        
        graph[i].append(adj)

topoOrdering = topoSort(graph)

probs = {}
probs[N] = 1

for vertex in topoOrdering:
    if len(graph[vertex]) > 0:
        probs[vertex] = sum(map(lambda x: probs[x], graph[vertex])) / len(graph[vertex])
    elif vertex != N:
        probs[vertex] = 0

print(probs[coords[0][0][1]])