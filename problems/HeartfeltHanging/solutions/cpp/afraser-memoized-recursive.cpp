#include <algorithm>
#include <iostream>

using namespace std;

int recursiveSolve(int athlete, int length, int budget, int *train, int *scores, int **memo) {
    if (athlete == length) {
        return 0;
    }

    if (memo[athlete][budget] != -1) {
        return memo[athlete][budget];
    }

    int dontPick = recursiveSolve(athlete + 1, length, budget, train, scores, memo);
    int pick;
    
    if (budget >= train[athlete]) {
        pick = recursiveSolve(athlete + 1, length, budget - train[athlete], train, scores, memo) + scores[athlete]; 
    }
    else {
        pick = -1;
    }

    int result = max(dontPick, pick);
    memo[athlete][budget] = result;
    
    return result;
}

int solve(int length, int budget, int *train, int *scores) {
    int **memo = new int*[length];

    for (int i = 0; i < length; i++) {
        memo[i] = new int[budget + 1];
        for (int j = 0; j < budget + 1; j++) {
            memo[i][j] = -1;
        }
    }

    return recursiveSolve(0, length, budget, train, scores, memo);
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