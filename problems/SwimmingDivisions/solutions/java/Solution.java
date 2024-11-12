import java.util.*;
import java.io.*;

public class Solution {
    // Union-Find structure with top-ranked tracking
    static class UnionFind {
        int[] parent;
        int[] topRanked;

        public UnionFind(int size) {
            parent = new int[size];
            topRanked = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
                topRanked[i] = i;
            }
        }

        // Find with path compression
        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        // Union multiple sets and set topRanked to winner
        public void union(List<Integer> roots, int winner) {
            int targetRoot = roots.get(0);
            for (int i = 1; i < roots.size(); i++) {
                parent[roots.get(i)] = targetRoot;
            }
            topRanked[targetRoot] = winner;
        }
    }

    public static void main(String[] args) throws IOException {
        // Fast input and output
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // Read number of competitors
        int N = Integer.parseInt(br.readLine().trim());

        // Map competitor names to unique IDs and store names
        Map<String, Integer> nameToId = new HashMap<>(N);
        String[] idToName = new String[N];
        for (int i = 0; i < N; i++) {
            String name = br.readLine().trim();
            nameToId.put(name, i);
            idToName[i] = name;
        }

        // Initialize Union-Find
        UnionFind uf = new UnionFind(N);

        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.equals("END")) {
                break;
            }
            if (line.startsWith("COMPETITION")) {
                // Parse competition
                String[] parts = line.split("\\s+");
                int M = Integer.parseInt(parts[1]);

                List<Integer> participants = new ArrayList<>(M);
                for (int i = 0; i < M; i++) {
                    String participant = br.readLine().trim();
                    participants.add(nameToId.get(participant));
                }

                // Winner is the first participant
                int winnerId = participants.get(0);

                // Find unique roots
                Set<Integer> uniqueRootsSet = new HashSet<>();
                for (int id : participants) {
                    uniqueRootsSet.add(uf.find(id));
                }
                List<Integer> uniqueRoots = new ArrayList<>(uniqueRootsSet);

                // If more than one unique root, merge them
                if (uniqueRoots.size() > 1) {
                    uf.union(uniqueRoots, winnerId);
                } else {
                    // Even if already in one set, update the top-ranked to winner
                    int root = uniqueRoots.get(0);
                    uf.topRanked[root] = winnerId;
                }
            } else if (line.startsWith("REQUEST")) {
                // Parse request
                String[] parts = line.split("\\s+");
                String requester = parts[1];
                int requesterId = nameToId.get(requester);
                int root = uf.find(requesterId);
                int topRankedId = uf.topRanked[root];
                bw.write(idToName[topRankedId]);
                bw.newLine();
            }
        }

        // Flush the output
        bw.flush();
    }
}
