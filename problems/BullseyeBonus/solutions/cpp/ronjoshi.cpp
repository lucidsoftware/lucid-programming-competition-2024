using namespace std;
#include <iostream>
#include <vector>
#include <cmath>

int n;

// segment tree. Pair stores (sum, count) of the segment
vector<pair<int, int>> t; 
vector<int> scores;

void build(int v, int tl, int tr) {
    if(tl == tr) {
        t[v] = {scores[tl], 1};
    } else {
        int tm = (tl + tr) / 2;
        build(v*2, tl, tm);
        build(v*2+1, tm+1, tr);
        t[v] = {t[v*2].first + t[v*2+1].first, t[v*2].second + t[v*2+1].second};
    }
}

pair<int, int> find(int v, int tl, int tr, int l, int r) {
    if(l > r) return {0, 0};
    if(l == tl && r == tr) return t[v];

    int tm = (tl + tr) / 2;

    auto s1 = find(v*2, tl, tm, l, min(r, tm));
    auto s2 = find(v*2 + 1, tm+1, tr, max(l, tm+1), r);

    return {s1.first + s2.first, s1.second + s2.second};
}

void update(int v, int tl, int tr, int pos, int new_val) {
    if(tl == tr) t[v].first = new_val;
    else {
        int tm = (tl + tr) / 2;
        if(pos <= tm) update(v*2, tl, tm, pos, new_val);
        else update(v*2 + 1, tm+1, tr, pos, new_val);

        auto s1 = t[v*2];
        auto s2 = t[v*2+1];

        t[v] = {s1.first + s2.first, s1.second + s2.second};
    }
}

int main() {
    int m; cin >> n >> m;

    t.resize(4*n);
    scores.resize(n);

    for(int i = 0; i < n; i++) {
        cin >> scores[i];
    }

    build(1, 0, n-1);

    for(int i = 0; i < m; i++) {
        int x, y, l, r; cin >> x >> y >> l >> r;
        x--; y--; l--; r--;

        auto p = find(1, 0, n-1, l, r);
        int avg = floor((double)p.first / (double)p.second);

        scores[x] += avg;
        scores[y] -= avg;

        update(1, 0, n-1, x, scores[x]);
        update(1, 0, n-1, y, scores[y]);
    }

    int max_i = 0;
    int max_score = scores[0];
    for(int i = 1; i < n; i++) {
        if(scores[i] > max_score) {
            max_score = scores[i];
            max_i = i;
        }
    }

    cout << max_i + 1 << endl;
}
