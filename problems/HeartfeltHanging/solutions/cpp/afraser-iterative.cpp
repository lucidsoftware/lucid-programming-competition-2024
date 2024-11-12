#include <algorithm>
#include <iostream>

using namespace std;

int solve(int length, int budget, int *train, int *scores) {
    int **memo = new int*[length + 1];

    for (int i = 0; i < length + 1; i++) {
        memo[i] = new int[budget + 1];
    }

    for (int j = 0; j < budget + 1; j++) {
        memo[length][j] = 0;
    }

    for (int i = length - 1; i >= 0; i--) {
        for (int j = 0; j < budget + 1; j++) {
            int dontPick = memo[i+1][j];
            int pick;
            if (j >= train[i]) {
                pick = memo[i+1][j - train[i]] + scores[i];
            }
            else {
                pick = -1;
            }
            memo[i][j] = max(dontPick, pick);
        }
    }

    return memo[0][budget];
}

int main() {
    int s, a;
    cin >> s;
    cin >> a;

    int *train = new int[a];
    int *scores = new int[a];

    for (int i = 0; i < a; i++)
        cin >> train[i];
    
    for (int i = 0; i < a; i++)
        cin >> scores[i];

    cout << solve(a, s, train, scores);
    
    return 0;
}