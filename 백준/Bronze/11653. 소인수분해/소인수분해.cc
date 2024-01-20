#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int x = 2;
    if (n == 1)
        return 0;
    for (int i = 2; i <= n; i++) {
        while (n % i == 0) {
            cout << i << endl;
            n /= i;
        }
    }
}