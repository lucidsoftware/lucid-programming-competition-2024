#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;
int main() {
    int num_logs; cin >> num_logs;
    unordered_map<string, int> dinosaurs;
    unordered_map<int, unordered_set<string> > holes;
    for (auto i = 0; i < num_logs; i++) {
        string dinosaur; cin >> dinosaur;
        int hole; cin >> hole;
        int prev_hole = dinosaurs[dinosaur];
        if (prev_hole) {
            holes[prev_hole].erase(dinosaur);
        }
        if (hole) {
            dinosaurs[dinosaur] = hole;
            holes[hole].insert(dinosaur);
        } else {
            dinosaurs.erase(dinosaur);
        }
    }
    vector<int> sorted_holes; sorted_holes.reserve(holes.size());
    for (auto& [hole, hole_dinosaurs]: holes) {
        sorted_holes.push_back(hole);
    }
    sort(sorted_holes.begin(), sorted_holes.end());
    for (auto hole: sorted_holes) {
        cout << hole << ' ';
        auto& hole_dinosaurs = holes[hole];
        int num_dino = hole_dinosaurs.size();
        if (num_dino) {
            vector<string> sorted_dinos; sorted_dinos.reserve(num_dino);
            for (auto& dino: hole_dinosaurs) {
                sorted_dinos.push_back(dino);
            }
            sort(sorted_dinos.begin(), sorted_dinos.end());
            for (int i = 0; i < num_dino; i++) {
                cout << sorted_dinos[i];
                if (i != num_dino - 1) {
                    cout << ' ';
                }
            }
        } else {
            cout << "n/a";
        }
        cout << '\n';
    }
    return 0;
}
