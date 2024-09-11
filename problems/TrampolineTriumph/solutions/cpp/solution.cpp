#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
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

double get_score(const vector<double>& milestone, double factor) {
    double local_maxima = get_local_maxima(milestone[0], milestone[1], factor);
    double local_maxima_value = get_position(local_maxima, factor);
    return local_maxima_value >= milestone[2] ? local_maxima_value : 0;
}

int main() {
    int players_count; cin >> players_count;
    
    vector<double> factors(players_count);
    for (int i = 0; i < players_count; ++i) {
        cin >> factors[i];
    }
    
    int milestones_count; cin >> milestones_count;
    
    vector<vector<double>> milestones(milestones_count, vector<double>(3));
    for (int i = 0; i < milestones_count; ++i) {
        cin >> milestones[i][0] >> milestones[i][1] >> milestones[i][2];
    }
    
    vector<double> scores(players_count, 0);
    for (const auto& milestone : milestones) {
        for (int i = 0; i < players_count; ++i) {
            scores[i] += get_score(milestone, factors[i]);
        }
    }
    
    vector<pair<int, double>> sorted_scores(players_count);
    for (int i = 0; i < players_count; ++i) {
        sorted_scores[i] = {i + 1, scores[i]};
    }
    
    sort(sorted_scores.begin(), sorted_scores.end(), [](const auto& a, const auto& b) {
        return b.second < a.second;
    });
    
    for (const auto& score : sorted_scores) {
        cout << score.first << endl;
        cout << fixed << setprecision(6) << score.second << endl;
    }
    
    return 0;
}
