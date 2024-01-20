#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, b;
    cin >> n >> b;
    string s;
    while (n != 0) {
        int x = n % b;
        if (x > 9) {
            x = x - 10 + 'A';
            s += x;
        }
        else {
            x += '0';
            s += x;
        }
        n /= b;
    }
    reverse(s.begin(), s.end());
    cout << s;
    return 0;
}