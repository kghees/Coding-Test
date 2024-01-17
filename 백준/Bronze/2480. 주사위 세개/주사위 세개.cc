#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int res = 0;
    if (a == b && b == c) {
        res = 10000 + a * 1000;
    }
    else if (a == b || a == c) {
        res = 1000 + a * 100;
    }
    else if (b == c) {
        res = 1000 + b * 100;
    }
    else {
        res = max(max(a, b), c) * 100;
    }
    cout << res;
    return 0;
}