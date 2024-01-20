#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n ,res = 0;
    cin >> n;
    for (int i = 2; i <= n; res++) {
        i += 6 * res;
    }
    if (n == 1) res = 1;
    cout << res;
    return 0;
}