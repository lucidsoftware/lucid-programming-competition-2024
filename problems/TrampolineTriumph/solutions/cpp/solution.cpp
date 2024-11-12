#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

double get_position(double x, double factor) {
    return (6 - 2 * factor * sin(x / 2) 
              - 2 * factor * sin(x / 5) 
              - 2 * factor * sin(x / 7)) * (0.9 + (1 + sin(x * factor / 3)) / 20);
}

double get_local_maxima(double l, double r, double factor) {
    while (r - l > 1e-9) {
        double m1 = l + (r - l) / 3;
        double m2 = r - (r - l) / 3;
        if (get_position(m1, factor) > get_position(m2, factor)) {
            r = m2;
        } else {
            l = m1;
        }
    }
    return l;
}

double get_jump_distance(const vector<double>& milestone, double factor) {
    double local_maxima = get_local_maxima(milestone[0], milestone[1], factor);
    return get_position(local_maxima, factor);
}

vector<int> get_scores(const vector<vector<double>>& milestones, const vector<double>& factors) {
    int players_count = factors.size();
    vector<int> scores(players_count, 0);
    for (const auto& milestone : milestones) {
        double max_jump_distance = -1;
        int winner = -1;
        for (int i = 0; i < players_count; ++i) {
            double jump_distance = get_jump_distance(milestone, factors[i]);
            if (max_jump_distance == -1 || jump_distance > max_jump_distance) {
                max_jump_distance = jump_distance;
                winner = i;
            } else if (jump_distance == max_jump_distance) {
                cerr << "Error: multiple winners" << endl;
            }
        }
        if (winner != -1) {
            scores[winner] += 1;
        }
    }
    return scores;
}

int main() {
    int players_count; cin >> players_count;
    
    vector<double> factors(players_count);
    for (int i = 0; i < players_count; ++i) {
        cin >> factors[i];
    }

    int milestones_count; cin >> milestones_count;
    
    vector<vector<double>> milestones(milestones_count, vector<double>(2));
    for (int i = 0; i < milestones_count; ++i) {
        cin >> milestones[i][0] >> milestones[i][1];
    }

    vector<int> scores = get_scores(milestones, factors);
    vector<pair<int, int>> sorted_scores(players_count);
    for (int i = 0; i < players_count; ++i) {
        sorted_scores[i] = {i + 1, scores[i]};
    }

    sort(sorted_scores.begin(), sorted_scores.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) {
            return a.second > b.second;
        }
        return a.first < b.first;
    });

    for (const auto& score : sorted_scores) {
        cout << score.first << " " << score.second << endl;
    }

    return 0;
}
