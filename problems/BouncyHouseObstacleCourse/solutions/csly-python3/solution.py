import sys
import heapq

if __name__ == "__main__":
    # Parse input - O(V + E)
    num_nodes = int(input())
    nodes = {}
    start = None
    end = None
    for i in range(num_nodes):
        node = str(input())
        nodes[node] = []
        if start is None:
            start = node
        if i == num_nodes - 1:
            end = node
    num_edges = int(input())
    for _ in range(num_edges):
        s, d, w = input().split()
        source, dest, weight = str(s), str(d), int(w)
        nodes[source].append((dest, weight))
        nodes[dest].append((source, weight))

    # Dijkstra's algorithm using a priority queue - O((V + E) log V)
    distances = {node: sys.maxsize for node in nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in nodes}
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in nodes[current_node]:
            distance = current_distance + weight + (current_distance // 10)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    
    print(distances[end])
    for i in range(len(path)):
        print(path[i])