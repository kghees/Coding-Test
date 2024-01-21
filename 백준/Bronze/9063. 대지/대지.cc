#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, a,b;
    cin >> n;
    int x = -100000, y = 100000,w=-100000,z=100000;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        if (a > x)
            x = a;
        if (a < y)
            y = a;
        if (b > w)
            w = b;
        if (b < z)
            z = b;
    }
    cout << (x - y) * (w - z);
    return 0;
}