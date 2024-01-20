#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n,cnt = 0,a;
    cin >> n;
    while (n--) {
        cin >> a;
        int x = 0;
        if (a == 1)
            continue;
        else {
            for (int i = 2; i < a; i++) {
                if (a % i == 0) {
                    x = 1;
                    break;
                }
            }
            if (x) continue;
            else cnt++;
        }
    }
    cout << cnt;
    return 0;
}