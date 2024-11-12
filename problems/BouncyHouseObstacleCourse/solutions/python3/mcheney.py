# Dijkstra's

from collections import defaultdict

N = int(input())
if N > 10000:
    print("N is too big!")
    print(N)
    exit(1)
nodesList = []
for n in range(N):
    nodesList.append(input())

startNode = nodesList[0]
endNode = nodesList[-1]
nodes = defaultdict(list)

E = int(input())
if E > 50000:
    print("E is too big!")
    print(E)
    exit(1)
for e in range(E):
    line = input().split(' ')
    nodes[line[0]].append([line[1], int(line[2])]) # [name, cost]
    nodes[line[1]].append([line[0], int(line[2])]) # [name, cost]
    if int(line[2]) > 50:
        print("cost is too big!")
        print(line)
        exit(1)

def solve(doPrint=True):

    nodetoPrev = {} # which node did we come from to get to this node with min cost?
    neighbors = {} # node -> cost
    visited = set()

    def getClosestNeighbor():
        minNeighbor = None
        minCost = float('inf')
        for k, v in neighbors.items():
            if v < minCost:
                minNeighbor = k
                minCost = v
        return minNeighbor, minCost

    node = ""
    cost = 0
    neighbors[startNode] = 0
    while len(neighbors) > 0:
        node, cost = getClosestNeighbor()
        if node == endNode:
            break
        neighbors.pop(node)
        cost += cost // 10
        visited.add(node)
        for [neighbor, neighborCost] in nodes[node]:
            if neighbor in visited:
                continue
            realNeighborCost = neighborCost  + cost
            if neighbor not in neighbors or realNeighborCost < neighbors[neighbor]:
                neighbors[neighbor] = realNeighborCost
                nodetoPrev[neighbor] = node

    if doPrint:
        print(cost)
    path = [endNode]
    cur = endNode
    while cur in nodetoPrev:
        cur = nodetoPrev[cur]
        path.append(cur)
    if doPrint:
        pass
        # print(*reversed(path), sep="\n")
    return cost, path[::-1]

solve()

# final_cost, final_path = solve()
# for i in range(len(final_path) - 1):
#     # Break each link and see if we can find another path
#     nodeA = final_path[i]
#     nodeB = final_path[i+1]
#     oldNodesA = nodes[nodeA]
#     newNodesA = []
#     for [n, c] in nodes[nodeA]:
#         if n != nodeB:
#             newNodesA.append([n, c])
#     nodes[nodeA] = newNodesA
#     newNodesB = []
#     # for [n, c] in nodes[nodeB]:
#     #     if n != nodeA:
#     #         newNodesB.append([n, c])
#     # nodes[nodeB] = newNodesB
#     new_final_cost, new_final_path = solve(False)
#     nodes[nodeA] = oldNodesA
#     if new_final_cost == final_cost:
#         print("found duplicate path!")
#         print(nodeA, nodeB)
