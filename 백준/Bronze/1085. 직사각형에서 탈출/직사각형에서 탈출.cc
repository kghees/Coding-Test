#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    int res = min(min((w - x), (x - 0)), min((h-y),(y-0)));
    cout << res;
    return 0;
}