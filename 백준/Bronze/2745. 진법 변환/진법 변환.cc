#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    string n;
    int b, sum = 0;
    cin >> n >> b;
    for (int i = 0; i < n.length(); i++) {
        int x = n[n.length() - (i + 1)];
        if (x >= '0' && x <= '9') {
            x = x - '0';
        }
        else {
            x = x + 10 - 'A';
        }
        sum += (x * (int)pow(b,i));
    }
    cout << sum;
    return 0;
}