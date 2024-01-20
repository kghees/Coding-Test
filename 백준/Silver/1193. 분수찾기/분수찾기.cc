#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int x;
    cin >> x;
    int i = 1;
    while (x > i) {
        x -= i;
        i++;
    }
    if (i % 2 == 0)
        cout << x << "/" << i + 1 - x;
    else
        cout << i + 1 - x << "/" << x;
    return 0;
}