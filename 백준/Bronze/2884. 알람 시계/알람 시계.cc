#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (b < 45) {
        a -= 1;
        b += 15;
    }
    else
        b -= 45;
    if (a < 0)
        a = 23;
    cout << a << " " << b;
    return 0;
}