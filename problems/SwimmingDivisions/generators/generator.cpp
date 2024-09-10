using namespace std;
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
#include <set>

bool debug = true;
int N_MAX = 100000;

// Create a random device to seed the random number generator
std::random_device rd;
// Use the Mersenne Twister engine for generating random numbers
std::mt19937 gen(rd());

int getRandomInt(int min, int max) {
    // Define the distribution range for the random numbers
    std::uniform_int_distribution<> dist(min, max);
    // Generate and return a random number within the specified range
    return dist(gen);
}

pair<int, int> idx_to_chunk_range(int i, vector<int> &starts, int n_used) {
    int start = starts[i];
    int end = i == starts.size() - 1 ? n_used - 1 : starts[i + 1] - 1;
    return make_pair(start, end);
}

vector<int> create_chunks(int n, int num_ignore, vector<int> &req_chunk_sizes) {
    vector<int> starts;
    int curr_sum = 0;
    for(int i = 0; i < req_chunk_sizes.size(); i++) {
        int k = req_chunk_sizes[i];
        starts.push_back(curr_sum);
        curr_sum += k;
    }
    if(curr_sum < n - 1) {
        starts.push_back(curr_sum);
        int remaining = n - curr_sum - num_ignore;
        int chunk_size = sqrt(remaining);
        for(int i = chunk_size;; i += chunk_size) {
            if(curr_sum + i >= n - num_ignore) break;
            starts.push_back(curr_sum + i);
        }
    }

    if(debug) {
        cout << "Starts: ";
        for(int i : starts) {
            cout << i << " ";
        }
        cout << endl;
    }

    return starts;
}


/*
Inputs: start and end are the contestant IDs, inclusive, that belong to the chunk.

Output: A list of inputs for the chunk. If inputs[i] is a list of 1 number, it's a request for the contestant with that ID.
If it's a list of >1 items, then it's a competition between the contestants in the list.
*/
vector<vector<int>> create_inputs_for_chunk(int start, int end) {
    vector<vector<int>> inputs;

    // A set to store which contestants have been chosen
    vector<bool> chosen_set(end - start + 1, false);
    // A list of chosen competitors
    vector<int> chosen;

    for(int k = start + 1; k <= end; k++) {
        // From the range [start, k], contestants are randomly chosen to compete in a competition.
        vector<int> competing;
        for(int i = start; i <= k; i++) {
            if(
                k == end // If we're at the end, we make a competition with everyone in this chunk so we ensure connectivity of this set
                || (i >= k-1 && competing.size() < 2) // At least 2 contestants must compete
                || (getRandomInt(0, 1) == 1) // Each contestant has 50% chance of being chosen
            ) {
                competing.push_back(i);
                if(!chosen_set[i-start]) {
                    chosen_set[i - start] = true;
                    chosen.push_back(i);
                }
            }
        }
        shuffle(competing.begin(), competing.end(), gen);
        inputs.push_back(competing);

        // After creating a competition, we make a few requests to random contestants in the chunk
        int n_requests = getRandomInt(1, 5);
        for(int i = 0; i < n_requests; i++) {
            int req_idx = getRandomInt(0, chosen.size() - 1);
            inputs.push_back({chosen[req_idx]});
        }
    }

    return inputs;
}



void print_inputs_all_chunks(vector<vector<vector<int>>> all_inputs, vector<int> &i2n, vector<string> &names, std::ofstream &outFile) {
    int n_chunks = all_inputs.size();

    // The number of inputs read from each chunk
    vector<int> n_inputs_read(n_chunks, 0);

    // Loop through all the inputs in order, and shuffle them by chunk.
    // i.e. within-chunk inputs keep order, but inputs from different chunks are shuffled.
    while(n_chunks > 0) {
        int chosen_chunk = getRandomInt(0, n_chunks - 1);
        
        vector<int> next_input = all_inputs[chosen_chunk][n_inputs_read[chosen_chunk]];

        if(next_input.size() == 1) {
            outFile << "REQUEST " << names[i2n[next_input[0]]] << endl;
        } else {
            outFile << "COMPETITION " << next_input.size() << endl;
            for(int i : next_input) {
                outFile << names[i2n[i]] << endl;
            }
        }

        n_inputs_read[chosen_chunk]++;
        if(n_inputs_read[chosen_chunk] == all_inputs[chosen_chunk].size()) {
            all_inputs[chosen_chunk] = all_inputs[n_chunks - 1];
            n_inputs_read[chosen_chunk] = n_inputs_read[n_chunks - 1];
            n_chunks--;
        }
    }
}

void print_chunk_combinations(vector<pair<vector<int>, vector<int>>> combined_inputs, std::ofstream &outFile, vector<int> &i2n, vector<string> &names) {
    for(auto [competing, requests] : combined_inputs) {
        outFile << "COMPETITION " << competing.size() << endl;
        for(int i : competing) {
            outFile << names[i2n[i]] << endl;
        }
        for(int i : requests) {
            outFile << "REQUEST " << names[i2n[i]] << endl;
        }
    }
}

void combine_chunks(vector<vector<vector<int>>> &INPUTS, vector<int> &starts, int n, int num_ignore, int combine_all_chunks, vector<int> &i2n, vector<string> &names, std::ofstream &outFile) {
    int n_chunks = INPUTS.size();
    vector<pair<int, int>> chunk_idxs_to_combine;
    for(int i = 0; i < n_chunks; i++) chunk_idxs_to_combine.push_back({i, i});

    
    while(true) {
        if((!combine_all_chunks && chunk_idxs_to_combine.size() < 6) || (chunk_idxs_to_combine.size() == 1)) {
            break;
        }

        vector<pair<vector<int>, vector<int>>> combined_inputs_for_sweep;

        // Combine pairs of chunk ranges, and print output to file
        // Each sweep combines chunk ranges in pairs
        vector<pair<int, int>> new_chunk_idxs;
        for(int i = 0; i < chunk_idxs_to_combine.size(); i += 2) {
            // a, b are the indices of the chunks to combine
            int a, b;
            if(i == n_chunks - 1) {
                a = chunk_idxs_to_combine[i].first;
                b = chunk_idxs_to_combine[i].second;
            } else {
                a = chunk_idxs_to_combine[i].first;
                b = chunk_idxs_to_combine[i + 1].second;
            }
            new_chunk_idxs.push_back({a, b});

            auto [start_a, end_a] = idx_to_chunk_range(a, starts, n - num_ignore);
            auto [start_b, end_b] = idx_to_chunk_range(b, starts, n - num_ignore);

            // start and end are the indices of the contestants in the combined chunk
            auto [start, end] = make_pair(start_a, end_b);

            vector<int> competing;

            // One from each chunk range is guaranteed to be chosen so that the two ranges are connected
            int rnd_choice_1 = getRandomInt(start_a, end_a);
            int rnd_choice_2 = getRandomInt(start_b, end_b);
            competing.push_back(rnd_choice_1); competing.push_back(rnd_choice_2);

            for(int j = start; j <= end; j++) {
                if(j == rnd_choice_1 || j == rnd_choice_2) continue;
                if(
                    (getRandomInt(0, 1) == 1) // Each contestant has 50% chance of being chosen
                ) {
                    competing.push_back(j);
                }
            }
            shuffle(competing.begin(), competing.end(), gen);

            // After creating a competition, we make a few requests to random contestants in the chunk
            int n_requests = getRandomInt(1, 5);
            vector<int> requests;
            for(int j = 0; j < n_requests; j++) {
                int req_idx = getRandomInt(0, competing.size() - 1);
                requests.push_back({req_idx});
            }

            combined_inputs_for_sweep.push_back(make_pair(competing, requests));
        }
        chunk_idxs_to_combine = new_chunk_idxs;

        shuffle(combined_inputs_for_sweep.begin(), combined_inputs_for_sweep.end(), gen);
        print_chunk_combinations(combined_inputs_for_sweep, outFile, i2n, names);
    }
}

/*
nc: number of contestants
num_ignore: number of contestants to ignore (they never compete)
req_chunk_sizes: the sizes of the chunks that must be formed. If the sum of these != n, then the 
    rest of the contestants will be put in chunks of size sqrt(n_remaining), where n_remaining = n - sum(req_chunk_sizes)
names: the names of the contestants. This is made a reference parameter so that we can use the same names across test cases
should_combine_chunks: whether to combine chunks or not at the end
combine_all_chunks: whether to combine all of them into one big set. If false, then a few sets will remain disjoint.

*/
void createTestCase(
    int test_idx, 
    int n, 
    int num_ignore, 
    vector<int> req_chunk_sizes, 
    vector<string> &names,
    bool should_combine_chunks,
    bool combine_all_chunks
) {
    string filename = (test_idx < 10) ? "0" + to_string(test_idx) + ".in" : to_string(test_idx) + ".in";
    std::ofstream outFile(filename);

    // The start index of each chunk
    vector<int> starts = create_chunks(n, num_ignore, req_chunk_sizes);

    // Consolidate all inputs into one big chunk
    vector<vector<vector<int>>> INPUTS;

    for(int i = 0; i < starts.size(); i++) {
        // Get start and end values for this chunk
        auto [start, end] = idx_to_chunk_range(i, starts, n - num_ignore);

        // Create the inputs for this chunk
        vector<vector<int>> inputs = create_inputs_for_chunk(start, end);
        INPUTS.push_back(inputs);
    }

    // Shuffles the indices so that we get random names instead of the same names in the same order
    // To get the name for index i, we use names[i2n[i]]
    vector<int> i2n; // index to name
    for(int i = 0; i < n; i++) i2n.push_back(i);
    std::shuffle(i2n.begin(), i2n.end(), gen);

    // Print out the names
    outFile << n << endl;
    for(int i = 0; i < n; i++) {
        outFile << names[i2n[i]] << endl;
    }

    print_inputs_all_chunks(INPUTS, i2n, names, outFile);

    // Now we combine the chunks together.
    // Pairs of chunks are combined, so there's a total of log_2(n_chunks) rounds of combining.
    
    if(should_combine_chunks) {
        combine_chunks(INPUTS, starts, n, num_ignore, combine_all_chunks, i2n, names, outFile);
    }

    outFile << "END" << endl;
}

vector<string> make_names() {
    set<string> names_set;
    vector<string> names;
    for(int i = 0; i < N_MAX; i++) {
        string name = "";
        for(int j = 0; j < 10; j++) {
            name += (char)('a' + getRandomInt(0, 25));
        }
        if(names_set.find(name) == names_set.end()) {
            names_set.insert(name);
            names.push_back(name);
        }
    }
    return names;
}

int main() {
    vector<string> names = make_names();

    // createTestCase(
    //     4, // index
    //     100, // Number of contestants
    //     2, // num_ignore
    //     {20, 20, 20}, // req_chunk_sizes
    //     names, // contestant names
    //     true, // should_combine_chunks
    //     true // combine_all_chunks
    // );

    // createTestCase(
    //     5, // index
    //     2000, // Number of contestants
    //     0, // num_ignore
    //     {100, 2, 500, 700}, // req_chunk_sizes
    //     names, // contestant names
    //     true, // should_combine_chunks
    //     true // combine_all_chunks
    // );
    
    // createTestCase(
    //     6, // index
    //     20000, // Number of contestants
    //     10000, // num_ignore
    //     {5, 2, 100}, // req_chunk_sizes
    //     names, // contestant names
    //     false, // should_combine_chunks
    //     false // combine_all_chunks
    // );

    createTestCase(
        7, // index
        10000, // Number of contestants
        1000, // num_ignore
        {1000, 500, 2, 500, 1000}, // req_chunk_sizes
        names, // contestant names
        false, // should_combine_chunks
        false // combine_all_chunks
    );

    // createTestCase(
    //     8, // index
    //     10000, // Number of contestants
    //     0, // num_ignore
    //     {}, // req_chunk_sizes
    //     names, // contestant names
    //     true, // should_combine_chunks
    //     true // combine_all_chunks
    // );

    // createTestCase(
    //     9, // index
    //     40000, // Number of contestants
    //     0, // num_ignore
    //     {}, // req_chunk_sizes
    //     names, // contestant names
    //     true, // should_combine_chunks
    //     true // combine_all_chunks
    // );

    createTestCase(
        10, // index
        40000, // Number of contestants
        0, // num_ignore
        {}, // req_chunk_sizes
        names, // contestant names
        true, // should_combine_chunks
        false // combine_all_chunks
    );

    createTestCase(
        11, // index
        40000, // Number of contestants
        0, // num_ignore
        {}, // req_chunk_sizes
        names, // contestant names
        false, // should_combine_chunks
        false // combine_all_chunks
    );

    return 0;
}

