#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int res = 2;
    while (n--) {
        res = res * 2 - 1;
    }
    cout << res * res;
    return 0;
}