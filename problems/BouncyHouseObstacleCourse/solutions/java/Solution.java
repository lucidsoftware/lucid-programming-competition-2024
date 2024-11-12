import java.util.*;
import java.io.*;

public class Solution {
    // Class to represent an obstacle (edge)
    static class Obstacle {
        int to;
        int baseTime;

        Obstacle(int to, int baseTime) {
            this.to = to;
            this.baseTime = baseTime;
        }
    }

    // Class to represent entries in the priority queue
    static class State implements Comparable<State> {
        int node;
        long time;

        State(int node, long time) {
            this.node = node;
            this.time = time;
        }

        @Override
        public int compareTo(State other) {
            return Long.compare(this.time, other.time);
        }
    }

    public static void main(String[] args) {
        // For faster input reading
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        // Read number of nodes
        int numNodes = Integer.parseInt(br.readLine().trim());

        // Read node names and map them to unique IDs
        Map<String, Integer> nodeNameToId = new HashMap<>();
        String[] idToNodeName = new String[numNodes];
        for (int i = 0; i < numNodes; i++) {
            String nodeName = br.readLine().trim();
            nodeNameToId.put(nodeName, i);
            idToNodeName[i] = nodeName;
        }

        // Start node is node 0, end node is node (numNodes -1)
        int startNode = 0;
        int endNode = numNodes -1;

        // Read number of obstacles
        int numObstacles = Integer.parseInt(br.readLine().trim());

        // Build adjacency list
        List<Obstacle>[] adj = new ArrayList[numNodes];
        for (int i = 0; i < numNodes; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < numObstacles; i++) {
            line = br.readLine().trim();
            String[] parts = line.split("\\s+");
            String nodeA = parts[0];
            String nodeB = parts[1];
            int time = Integer.parseInt(parts[2]);

            int idA = nodeNameToId.get(nodeA);
            int idB = nodeNameToId.get(nodeB);

            adj[idA].add(new Obstacle(idB, time));
            adj[idB].add(new Obstacle(idA, time));
        }

        // Implement Dijkstra's algorithm
        long[] minTime = new long[numNodes];
        Arrays.fill(minTime, Long.MAX_VALUE);
        minTime[startNode] = 0;

        int[] predecessor = new int[numNodes];
        Arrays.fill(predecessor, -1);

        PriorityQueue<State> pq = new PriorityQueue<>();
        pq.offer(new State(startNode, 0));

        boolean[] visited = new boolean[numNodes];

        while (!pq.isEmpty()) {
            State current = pq.poll();
            int currentNode = current.node;
            long currentTime = current.time;

            if (visited[currentNode]) {
                continue;
            }
            visited[currentNode] = true;

            if (currentNode == endNode) {
                break;
            }

            for (Obstacle obstacle : adj[currentNode]) {
                int neighbor = obstacle.to;
                int baseTime = obstacle.baseTime;

                // Calculate additional time based on currentTime
                long additionalTime = currentTime / 10;
                long totalObstacleTime = baseTime + additionalTime;

                long newTime = currentTime + totalObstacleTime;

                if (newTime < minTime[neighbor]) {
                    minTime[neighbor] = newTime;
                    predecessor[neighbor] = currentNode;
                    pq.offer(new State(neighbor, newTime));
                }
            }
        }

        // Output the total time
        System.out.println(minTime[endNode]);
    }
}