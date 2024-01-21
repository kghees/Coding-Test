#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, res = 0;
    cin >> n;
    for (int i = 1; i < n; i++) {
        int sum = 0, num = i;
        while (num) {
            sum += num % 10;
            num /= 10;
        }
        sum += i;
        if(sum == n) {
            res = i;
            break;
        }
    }
    cout << res;
    return 0;
}