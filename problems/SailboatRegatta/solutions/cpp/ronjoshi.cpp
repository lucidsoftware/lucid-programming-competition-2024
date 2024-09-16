using namespace std;
#include <vector>
#include <iostream>
#include <queue>
#include <set>

bool debug = false;

struct Node {
    int vx;
    int vy;
    int x;
    int y;
    bool raised;
    int cooldown;

    bool operator<(const Node& other) const {
        return tie(vx, vy, x, y, raised, cooldown) < tie(other.vx, other.vy, other.x, other.y, other.raised, other.cooldown);
    }
};
struct Compare {
    bool operator()(const pair<int, Node>& p1, const pair<int, Node>& p2) {
        return p1.first > p2.first;
    }
};

vector<string> split(const string& str) {
    vector<string> result;
    string temp = "";
    for (char ch : str) {
        if (ch == ',') {
            if (!temp.empty()) {
                result.push_back(temp);
                temp.clear();
            }
        } else {
            temp += ch;
        }
    }
    if (!temp.empty()) {
        result.push_back(temp);
    }
    return result;
}

int w;
int l;
int k;

vector<vector<pair<int, int>>> grid;

int main() {
    cin >> w >> l >> k;
    grid = vector<vector<pair<int, int>>>(l+1, vector<pair<int, int>>(w+1));

    for(int i = 1; i <= l; i++) {
        for(int j = 1; j <= w; j++) {
            string s; cin >> s;
            vector<string> v = split(s);
            grid[i][j] = {stoi(v[0]), stoi(v[1])};
        }
    }

    priority_queue<pair<int, Node>, vector<pair<int, Node>>, Compare> pq;
    
    // stores tuples of seen states so far
    set<Node> visited;
    
    for(int j = 1; j <= w; j++) {
        pq.push({0, {0, 1, j, 1, true, 0}});
    }

    int ans = -1;

    while(!pq.empty()) {
        auto p = pq.top(); pq.pop();
        int t = p.first;
        Node node = p.second;

        if(visited.count(node)) {
            continue;
        }
        visited.insert(node);

        auto [vx, vy, x, y, raised, cooldown] = node;

        // Check for out of bounds
        if((x <= 0 || x > w) || y <= 0) {
            continue;
        }
        // Win condition
        if(y > l) {
            ans = t;
            break;
        }

        // Stay at current sail configuration
        int new_vx = vx + ((raised) ? grid[y][x].first : 0);
        int new_vy = vy + ((raised) ? grid[y][x].second : 0);

        pq.push({t + 1, 
            {
                new_vx,
                new_vy,
                x + new_vx,
                y + new_vy,
                raised,
                max(cooldown - 1, 0)
            }
        });

        if(cooldown == 0) {
            // Toggle sail configuration

            new_vx = vx + ((raised) ? 0 : grid[y][x].first);
            new_vy = vy + ((raised) ? 0 : grid[y][x].second);

            pq.push({t + 1, 
                {
                    new_vx,
                    new_vy,
                    x + new_vx,
                    y + new_vy,
                    !raised,
                    k - 1
                }
            });
        }
    }

    cout << ans + 1 << endl;
}
