using namespace std;

#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <iomanip>

bool debug = false;

struct Flipper {
    int x;
    int y;
    int i; // index of flipper
    vector<int> dxs;

    bool operator< (const Flipper &p) const {
		if(y != p.y) return (y < p.y);
		return x < p.x;
	}

    Flipper(int xVal, int yVal, int iVal, vector<int> dxVals) : x(xVal), y(yVal), i(iVal), dxs(dxVals) {}
};


vector<int> topoSort(vector<vector<int>>& adj) {
    int V = adj.size();          // Number of vertices

    vector<int> inDegree(V, 0);  // Vector to store the in-degree of each vertex
    vector<int> topoOrder;       // To store the topological order

    // Calculate in-degree (number of incoming edges) of each vertex
    for (int i = 0; i < V; i++) {
        for (int u : adj[i]) {
            inDegree[u]++;
        }
    }

    // Queue to store vertices with in-degree 0
    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    // Process vertices with in-degree 0
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        topoOrder.push_back(v);

        // Decrease the in-degree of all adjacent vertices of v
        for (int u : adj[v]) {
            inDegree[u]--;
            if (inDegree[u] == 0) {
                q.push(u);  // If in-degree becomes 0, add it to the queue
            }
        }
    }

    return topoOrder;
}


int main() {
    int n, L;
    cin >> n >> L;
    vector<Flipper> flippers;

    // Initialize the initial putt of the ball as a flipper with x displacement of 0
    flippers.push_back(Flipper(0, 0, 0, {0}));

    // layout[x] = {y1, y2, y3, ...} means there are flippers at (x, y1), (x, y2), (x, y3), ...
    map<int, set<Flipper>> layout;

    for(int i = 0; i < n; i++) {
        int x, y, nd; cin >> x >> y >> nd;

        vector<int> dxs;
        for(int j = 0; j < nd; j++) {
            int dx; cin >> dx;
            dxs.push_back(dx);
        }

        Flipper f(x, y, i + 1, dxs);

        flippers.push_back(f);
        if(layout.find(x) == layout.end()) layout[x] = set<Flipper>();
        layout[x].insert(f);
    }

    // Add an ending flipper for the hole. Obviously, it doesn't function as a flipper
    // but we will need to add it to the graph to make the calculation easy
    // as it is topologically the last "flipper" in the graph
    flippers.push_back(Flipper(0, L, n + 1, {}));
    layout[0].insert(flippers[n + 1]);
    n += 2;

    // print layout for debugging
    if(debug){for(auto it = layout.begin(); it != layout.end(); ++it) {
        cout << it->first << ": ";
        for(auto it2 = it->second.begin(); it2 != it->second.end(); ++it2) {
            cout << it2->y << " ";
        }
        cout << endl;
    }}

    // graph[i] = {j1, j2, j3, ...} means there is a path from i to j1, i to j2, i to j3, ...
    vector<vector<int>> graph;

    for(int i = 0; i < n; i++) {
        vector<int> adj;
        vector<int> dxs = flippers[i].dxs;

        for(int k = 0; k < dxs.size(); k++) {
            if(layout.find(flippers[i].x + dxs[k]) != layout.end()) {
                // Find the flipper with the smallest y value that is greater than flippers[i].y
                // that's the one flipper i will reach

                auto lb_it = layout[flippers[i].x + dxs[k]].lower_bound(Flipper(0, flippers[i].y, 0, {}));
                if(lb_it->y == flippers[i].y) {
                    cout << "ERROR: " << i << " (" << flippers[i].x << ", " << flippers[i].y << ") lands on " << lb_it->i << " (" << lb_it->x << ", " << lb_it->y << "), disp of " << dxs[k] << endl;
                }
                if(lb_it != layout[flippers[i].x + dxs[k]].end()) {
                    adj.push_back(lb_it->i);
                }
            }
        }

        graph.push_back(adj);
    }

    if(debug){cout << "Adjacency matrix:" << endl;
    for(int i = 0; i < n; i++) {
        cout << i << " (" << flippers[i].x << ", " << flippers[i].y << "): ";
        for(int j = 0; j < graph[i].size(); j++){
            cout << graph[i][j] << " (" << flippers[graph[i][j]].x << ", " << flippers[graph[i][j]].y << ") ";
        }
        cout << endl;
    }}

    vector<int> topo = topoSort(graph);

    if(debug){
        cout << "Topological order:" << endl;
        for(int i = 0; i < topo.size(); i++) {
            cout << topo[i] << ": (" << flippers[topo[i]].x << ", " << flippers[topo[i]].y << ") " << endl;
        }
    }

    // initial hit has 100% probability. Cumulatively add the probabilities of reaching each flipper
    // downwards on the topological order graph.
    vector<long double> probabilities(n, 0);
    probabilities[0] = 1;

    for(int k = 0; k < topo.size(); k++) {
        int i = topo[k];
        if(probabilities[i] == 0) continue;
        for(int j = 0; j < graph[i].size(); j++) {
            // probability of reaching flipper i splits into graph[i].size() paths (each one being equal)
            int child_idx = graph[i][j];
            probabilities[child_idx] += (long double) probabilities[i] / (long double) flippers[i].dxs.size();
        }
    }

    if(debug){
        cout << "Probabilities:" << endl;
        for(int i = 0; i < n; i++) {
            cout << i << ": " << probabilities[i] << endl;
        }
    }
    
    cout << setprecision(8);
    // This is the probability of reaching the hole (i.e. the last "flipper")
    cout << probabilities[n-1] << endl;
}