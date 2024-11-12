import heapq
import math

N = int(input())
graph = {}
start = None
end = None
for i in range(N):
    node = input()
    if i == 0:
        start = node
    if i == N - 1:
        end = node
    graph[node] = []

M = int(input())
for i in range(M):
    (startNode, endNode, cost) = input().split()
    graph[startNode].append((int(cost), endNode))
    graph[endNode].append((int(cost), startNode))

queue = []

heapq.heappush(queue, (0, (start, None)))

visited = set()
prevMap = {}
while len(queue) > 0:
    currTup = heapq.heappop(queue)
    currCost = currTup[0]
    currNode = currTup[1][0]
    prevNode = currTup[1][1]
    if currNode in visited:
        continue
    visited.add(currNode)
    prevMap[currNode] = prevNode
    if currNode == end:
        print(currCost)
        break
    deflateTime = math.floor(float(currCost) / 10.0)
    for adjTup in graph[currNode]:
        adjCost = adjTup[0]
        adjNode = adjTup[1]
        heapq.heappush(queue, (currCost + adjCost + deflateTime, (adjNode, currNode)))