import random

class Graph():
    #node distances is a dictionary of dictionaries, where the keys at both layer are the names of the nodes, and the values of the inner dictionary are the distance between the two nodes
    def __init__(self, nodes, nodeDistances):
        self.nodes = nodes
        self.graph = nodeDistances

    def getNeighbors(self, node):
        return list(self.graph[node].keys())

    def dijkstra(self,start):
        remainingNodes = self.nodes.copy()
        fastestTime = {}
        fastestPath = {}
        for node in remainingNodes:
            fastestTime[node] = 100000000001
        fastestTime[start] = 0

        while len(remainingNodes) > 0:
            bestKnownPath = None
            for node in remainingNodes:
                if (bestKnownPath == None) or (fastestTime[node] < fastestTime[bestKnownPath]):
                    bestKnownPath = node

            neighbors = self.getNeighbors(bestKnownPath)
            for neighbor in neighbors:
                # add extra seconds for bouncy house deflation
                newTime = fastestTime[bestKnownPath] + int(fastestTime[bestKnownPath]/10) + self.graph[bestKnownPath][neighbor]
                if newTime < fastestTime[neighbor]:
                    fastestTime[neighbor] = newTime
                    fastestPath[neighbor] = bestKnownPath
            remainingNodes.remove(bestKnownPath)
        
        return (fastestTime, fastestPath)

    def timeAndPath(self,start,finish):
        fastestTime, fastestPath = self.dijkstra(start)
        path = []
        node = finish
        
        while node != start:
            path.append(node)
            node = fastestPath[node]
        
        path.append(start)
        
        ret = str(fastestTime[finish])
        rev = reversed(path)
        for r in rev:
            ret += '\n' + r
        return ret

V = int(input())
vertices = []
for _ in range(V):
    vertices.append(input())
E = int(input())
nodes = dict()
for v in vertices:
    nodes[v] = dict()
for _ in range(E):
    obstacle = input()
    obstacleList = obstacle.split(" ")
    n1 = obstacleList[0]
    n2 = obstacleList[1]
    t = obstacleList[2]
    nodes[n1][n2] = t
    nodes[n2][n1] = t
G = graph(vertices,nodes)
print(G.timeAndPath(vertices[0],vertices[-1]))