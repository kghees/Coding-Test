#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int cnt = 0;
    while (n >= 0) {
        if (n % 5 == 0) {
            cnt += n / 5;
            n /= 5;
            cout << cnt << endl;
            break;
        }
        n -= 3;
        cnt += 1;
    }
    if (n < 0) {
        cout << -1;
    }
    return 0;
}