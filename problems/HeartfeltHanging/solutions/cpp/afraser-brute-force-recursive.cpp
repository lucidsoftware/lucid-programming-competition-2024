#include <algorithm>
#include <iostream>

using namespace std;

int recursiveSolve(int athlete, int length, int budget, int *train, int *scores) {
    if (athlete == length) {
        return 0;
    }

    int dontPick = recursiveSolve(athlete + 1, length, budget, train, scores);
    int pick;
    
    if (budget >= train[athlete]) {
        pick = recursiveSolve(athlete + 1, length, budget - train[athlete], train, scores) + scores[athlete]; 
    }
    else {
        pick = -1;
    }

    int result = max(dontPick, pick);
    
    return result;
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

    cout << recursiveSolve(0, a, s, train, scores);
    
    return 0;
}