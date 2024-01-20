#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int m, n, sum = 0, min = -1,cnt = 0;
    cin >> m >> n;
    for (int i = m; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            if (i % j == 0)
                cnt++;
        }
        if (cnt == 2) {
            sum += i;
            if (min == -1)
                min = i;
        }
        cnt = 0;
    }
    if (min == -1)
        cout << -1;
    else
        cout << sum << endl << min;
    return 0;
}