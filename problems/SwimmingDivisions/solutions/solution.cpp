#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

/*
Generated with ChatGPT lol. I just copy pasted python code and asked it to conver to cpp.
Might be efficient, but it's a good baseline for the "worst efficient solution"
*/


int find_set(vector<int>& link, int x) {
    if (x != link[x]) {
        link[x] = find_set(link, link[x]);
    }
    return link[x];
}

void unite(vector<int>& link, int x, int y) {
    link[find_set(link, x)] = y;
}

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vector<string> names(n);
    unordered_map<string, int> name_to_idx;

    for (int i = 0; i < n; ++i) {
        string name;
        getline(cin, name);
        names[i] = name;
        name_to_idx[name] = i;
    }

    vector<int> link(n);
    for (int i = 0; i < n; ++i) {
        link[i] = i;
    }

    string line;
    while (true) {
        getline(cin, line);
        if (line == "END") {
            break;
        }

        vector<string> tokens;
        string token;
        for (char ch : line) {
            if (ch == ' ') {
                tokens.push_back(token);
                token.clear();
            } else {
                token += ch;
            }
        }
        tokens.push_back(token); // push last token

        if (tokens[0] == "COMPETITION") {
            int n_compete = stoi(tokens[1]);

            int winner = -1;
            for (int i = 0; i < n_compete; ++i) {
                string name;
                getline(cin, name);
                int idx = name_to_idx[name];
                if (winner == -1) {
                    winner = idx;
                    int old_winner = find_set(link, winner);
                    link[winner] = winner;
                    unite(link, old_winner, winner);
                } else {
                    unite(link, idx, winner);
                }
            }
        } else if (tokens[0] == "REQUEST") {
            int idx = name_to_idx[tokens[1]];
            cout << names[find_set(link, idx)] << endl;
        }
    }

    return 0;
}
