#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int p, q;
    cin >> p >> q;
    int cnt = 0;
    int arr[10001] = {0};
    for (int i = 1; i <= p; i++) {
        if (p % i == 0) {
            arr[cnt] = i;
            cnt++;
        }
    }
    if (cnt >= q)
        cout << arr[q-1];
    else
        cout << 0;
    return 0;
}