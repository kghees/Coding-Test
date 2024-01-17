#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (b + c >= 60) {
        a =  (a+ (b + c) / 60) % 24;
        b = (b + c) % 60;
    }
    else {
        b += c;
    }
    cout << a << " " << b;
    return 0;
}