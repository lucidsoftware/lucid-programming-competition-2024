using namespace std;
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
#include <set>
#include <map>


// Parameters for test case generation

// Number of flippers
int n;

// Width of the board
int w;

// Height of the board
int h;

// Average number of flippers per x value. The true values are
// randomized, but they float around this average.
int avg_per_x;

// Ratio of useless x values to useful x values. Useless x values
// are those that don't have any flippers on them, and usefules ones
// are those that do
double num_non_keys_ratio;

// Ratio of displacements that (lead to a useful x value 
//  but don't lead to another flipper) to total useful x values
double n_key_to_offboard_ratio;

// The maximum what % of total flippers each flipper should reach
// (this value is randomized. This is just the upper bound)
double reach_flipper_ratio;

// Whether to include flippers at x = 0
bool include_at_0;

// Ratio of useful x values that should have a displacement to the hole
double reach_hole_ratio;


std::random_device rd;
std::mt19937 gen(rd());
std::ofstream outFile;
int getRandomInt(int min, int max) {
    // Define the distribution range for the random numbers
    std::uniform_int_distribution<> dist(min, max);
    // Generate and return a random number within the specified range
    return dist(gen);
}

void create_test_case() {
    // layout[x] = {y1, y2, y3, ...} means there are flippers at (x, y1), (x, y2), (x, y3), ...
    map<int, set<int>> layout;

    // all x values the flippers have. Assume it's sorted
    vector<int> layout_keys;
    // list of x values which are don't have any flippers
    vector<int> non_keys;

    // (x, y) coordinates of flippers
    vector<pair<int, int>> flippers;

    // dxs[i] has a list of all possible displacement flipper i can have. All with equal probability
    vector<vector<int>> all_dxs;

    // initialize flippers at x = 0 first.
    layout[0] = set<int>();
    layout_keys.push_back(0);
    if(include_at_0) {
        int n_flippers_at_0 = getRandomInt(max(1, (int)(0.5 * avg_per_x)), avg_per_x);
        int next_y_val = getRandomInt(2, 5);
        for(int i = 0; i < n_flippers_at_0; i++) {
            layout[0].insert(next_y_val);
            flippers.push_back({0, next_y_val});
            next_y_val += getRandomInt(1, max(1, h / (n_flippers_at_0 + 5)));
        }
    }

    // create flippers and their locations
    int loaded_so_far = layout[0].size();
    if(avg_per_x) {
        // about a fourth should be in random locations
        int max_grouped = 3*n / 4;

        while(loaded_so_far < max_grouped) {
            int x = getRandomInt(-w, w);

            while(layout.find(x) != layout.end()) {
                x = getRandomInt(-w, w);
            }

            layout[x] = set<int>();
            layout_keys.push_back(x);

            int n_grouped = getRandomInt(1, avg_per_x * 2);
            int avg_y_dist = h / n_grouped;

            int prev_loc = 0;
            for(int i = 0; i < n_grouped; i++) {
                int y = getRandomInt(prev_loc + avg_y_dist / 2, prev_loc + avg_y_dist);
                prev_loc = y;

                layout[x].insert(y);
                flippers.push_back({x, y});
            }

            loaded_so_far += n_grouped;
        }
    }
    
    for(int k = 0; k < n - loaded_so_far; k++) {
        int x = getRandomInt(-w, w);

        while(layout.find(x) != layout.end()) {
            x = getRandomInt(-w, w);
        }

        layout[x] = set<int>();
        layout_keys.push_back(x);
        int y = getRandomInt(0, h);
        layout[x].insert(y);
        flippers.push_back({x, y});
    }

    int n_useless_xs = num_non_keys_ratio * layout_keys.size();
    for(int k = 0; k < n_useless_xs; k++) {
        int x = getRandomInt(-w, w);

        while(layout.find(x) != layout.end()) {
            x = getRandomInt(-w, w);
        }

        non_keys.push_back(x);
    }

    // create connections for each flipper
    for(int i = 0; i < flippers.size(); i++) {
        // check which other flippers this one can reach
        auto [x1, y1] = flippers[i];

        vector<int> reachable_flipper_idxs;
        for(int j = 0; j < flippers.size(); j++) {
            if(i == j) continue;
            
            auto [x2, y2] = flippers[j];

            if(
                y2 > y1
                && (layout.find(x2) == layout.end() || layout[x2].count(y1) == 0)
            ) {
                // there is no flipper at (x2, y1). i can reach j
                reachable_flipper_idxs.push_back(j);
            }
        }
        
        shuffle(reachable_flipper_idxs.begin(), reachable_flipper_idxs.end(), gen);

        int n_to_reach = reachable_flipper_idxs.size() * reach_flipper_ratio;
        reachable_flipper_idxs.erase(reachable_flipper_idxs.begin() + n_to_reach + 1, reachable_flipper_idxs.end());

        vector<int> dxs;

        for(int j = 0; j < n_to_reach; j++) {
            // get the actual flipper index
            int k = reachable_flipper_idxs[j];

            dxs.push_back(flippers[k].first - x1);
        }

        // all displacement values that don't lead to a flipper
        for(int j = 0; j < layout_keys.size(); j++) {
            if(layout_keys[j] == x1) continue;
            if(layout_keys[j] == 0 && !include_at_0) continue;
            auto last_flipper_y = *(layout[layout_keys[j]].rbegin());

            if(
                last_flipper_y < y1
                && getRandomInt(0, 100) < n_key_to_offboard_ratio * 100
            ) {
                dxs.push_back(layout_keys[j] - x1);
            }
        }

        int n_useless_dxs = getRandomInt(0, non_keys.size()/2);
        shuffle(non_keys.begin(), non_keys.end(), gen);

        for(int j = 0; j < n_useless_dxs; j++) {
            dxs.push_back(non_keys[j] - x1);
        }

        // remove duplicates from dxs
        sort(dxs.begin(), dxs.end());
        auto it = unique(dxs.begin(), dxs.end());
        dxs.resize(distance(dxs.begin(), it));

        bool reach_hole_ratio_rand = (getRandomInt(0, 100) < reach_hole_ratio * 100);

        // debugfile << x1 << ", " << y1 << endl;
        // debugfile << (y1 == *(layout[x1].rbegin()) ? "Flipper is last in column" : "flipper not last in column") << endl;
        // debugfile << (layout[0].find(y1) == layout[0].end() ? "not found one there" : " found there") << endl;
        // debugfile << (find(dxs.begin(), dxs.end(), -x1) == dxs.end() ? "not found in dxs" : "found in dxs") << endl;
        // debugfile << reach_hole_ratio_rand << endl;

        if(
            x1 != 0 // flipper can't have displacement of 0
            && layout[0].find(y1) == layout[0].end() // displacement to 0 is illegal (another flipper there exists)
            && y1 == *(layout[x1].rbegin()) // This flipper is the last in its column
            && find(dxs.begin(), dxs.end(), -x1) == dxs.end() // it doesn't yet lead to the hole
            && reach_hole_ratio_rand // randomization
        ){
            // Let there be a displacement to the hole
            //debugfile << "disp to hole!" << endl;
            dxs.push_back(-x1);
        }
        
        shuffle(dxs.begin(), dxs.end(), gen);
        all_dxs.push_back(dxs);
    }

    vector<int> random_order;
    for(int i = 0; i < flippers.size(); i++) random_order.push_back(i);
    shuffle(random_order.begin(), random_order.end(), gen);

    outFile << flippers.size() << " " << h + 5 << endl;
    for(int k = 0; k < random_order.size(); k++) {
        // chooses a random flipper index to output
        int i = random_order[k];

        outFile << flippers[i].first << " " << flippers[i].second << " " << all_dxs[i].size() << endl;
        for(int j = 0; j < all_dxs[i].size(); j++) {
            outFile << all_dxs[i][j] << " ";
        }
        outFile << endl;
    }
}

int main() {
    // Basic test case. Very low connectivity
    outFile.open("05.in");
    n = 50;
    w = 20;
    h = 20;
    avg_per_x = 3;
    num_non_keys_ratio = 0.2;
    n_key_to_offboard_ratio = 0.3; 
    reach_flipper_ratio = 0.5;
    include_at_0 = true;
    reach_hole_ratio = 0.9;
    create_test_case();
    outFile.close();

    // High connectivity, low nodes
    outFile.open("06.in");
    n = 3000;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 0.001;
    n_key_to_offboard_ratio = 0.01;
    reach_flipper_ratio = 0.2;
    include_at_0 = true;
    reach_hole_ratio = 0.2;
    create_test_case();
    outFile.close();


    // Very low connectivity, high number of flippers
    outFile.open("07.in");
    n = 4000;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 0.01;
    n_key_to_offboard_ratio = 0.01;
    reach_flipper_ratio = 0.01;
    include_at_0 = false;
    reach_hole_ratio = 0.4;
    create_test_case();
    outFile.close();

    // Very narrow graph. Extremely low connectivity. Almost linear
    outFile.open("08.in");
    n = 9000;
    w = 4000;
    h = 1000000000;
    avg_per_x = 500;
    num_non_keys_ratio = 0.01;
    n_key_to_offboard_ratio = 0.01;
    reach_flipper_ratio = 0.01;
    include_at_0 = true;
    reach_hole_ratio = 0.1;
    create_test_case();
    outFile.close();

    // extremely high connectivity (almost all flippers can reach all other flippers)
    outFile.open("09.in");
    n = 1500;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 1;
    n_key_to_offboard_ratio = 1;
    reach_flipper_ratio = 1;
    include_at_0 = true;
    reach_hole_ratio = 1;
    create_test_case();
    outFile.close();

    // extremely high connectivity (almost all flippers can 
    // reach all other flippers). No flippers should go off the board.
    outFile.open("10.in");
    n = 2000;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 0;
    n_key_to_offboard_ratio = 0;
    reach_flipper_ratio = 1;
    include_at_0 = true;
    reach_hole_ratio = 1;
    create_test_case();
    outFile.close();

    // extremely high connectivity (almost all flippers can 
    // reach all other flippers). A tiny amount of flippers go
    // off the board.
    outFile.open("11.in");
    n = 2000;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 0.001;
    n_key_to_offboard_ratio = 0.001;
    reach_flipper_ratio = 1;
    include_at_0 = true;
    reach_hole_ratio = 1;
    create_test_case();
    outFile.close();

    // low nodes, high connectivity. No flippers at x = 0
    outFile.open("12.in");
    n = 3000;
    w = 1000000000;
    h = 1000000000;
    avg_per_x = 10;
    num_non_keys_ratio = 0.001;
    n_key_to_offboard_ratio = 0.01;
    reach_flipper_ratio = 0.2;
    include_at_0 = false;
    reach_hole_ratio = 0.2;
    create_test_case();
    outFile.close();

    // Very narrow, extremely low connectivity, high nodes
    // No flippers at x=0
    outFile.open("13.in");
    n = 9000;
    w = 4000;
    h = 1000000000;
    avg_per_x = 500;
    num_non_keys_ratio = 0.01;
    n_key_to_offboard_ratio = 0.01;
    reach_flipper_ratio = 0.01;
    include_at_0 = false;
    reach_hole_ratio = 0.1;
    create_test_case();
    outFile.close();

    // Narrow graph, low nodes. High number of displacements that lead
    // nowhere (i.e. off the board)
    outFile.open("14.in");
    n = 3000;
    w = 4000;
    h = 1000000000;
    avg_per_x = 500;
    num_non_keys_ratio = 1;
    n_key_to_offboard_ratio = 1;
    reach_flipper_ratio = 0;
    include_at_0 = true;
    reach_hole_ratio = 0;
    create_test_case();
    outFile.close();
}