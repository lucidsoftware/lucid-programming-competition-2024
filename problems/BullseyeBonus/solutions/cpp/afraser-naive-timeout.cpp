#include <iostream>
#include <cmath>

using namespace std;

int flooredAverage(int* arr, int left, int right) {
    int total = 0;
    for (int i = left; i <= right; i++) {
        total = total + arr[i];
    }

    long double floatTotal = total;
    long double divisor = right - left + 1;
    int result = floor(floatTotal / divisor);
    return result;
}

int maximumIndexOfArr(int* arr, int length) {
    int currentMax = arr[0];
    int currentMaxIndex = 0;

    for (int i = 1; i < length; i++) {
        if (arr[i] > currentMax) {
            currentMax = arr[i];
            currentMaxIndex = i;
        }
    }
        
    
    return currentMaxIndex;
}

int main() {
    int n, m;
    cin >> n >> m;

    int *archers = new int[n];
    
    for (int i = 0; i < n; i++)
        cin >> archers[i];

    for (int j = 0; j < m; j++) {
        int x, y, l, r;
        cin >> x >> y >> l >> r;
        int modifier = flooredAverage(archers, l - 1, r - 1);
        archers[x - 1] = archers[x - 1] + modifier;
        archers[y - 1] = archers[y - 1] - modifier;
    }

    cout << maximumIndexOfArr(archers, n) + 1;

    return 0;
}