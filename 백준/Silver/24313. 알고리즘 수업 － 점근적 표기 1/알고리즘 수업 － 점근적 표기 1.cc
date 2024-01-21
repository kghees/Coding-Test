#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int a1, a0, c, n;
    cin >> a1 >> a0 >> c >> n;
    if (a1 * n + a0 <= c*n && a1 <= c)
        cout << 1;
    else
        cout << 0;
    return 0;
}