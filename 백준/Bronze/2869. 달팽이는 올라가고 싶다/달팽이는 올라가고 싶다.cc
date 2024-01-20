#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int a, b, v, res = 0,day=1;
    cin >> a >> b >> v;
    day += (v - a) / (a - b);
    if ((v - a) % (a - b) != 0)
        day++;
    if (a >= v)
        cout << 1;
    else
        cout << day;
    return 0;
}