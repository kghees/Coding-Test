#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a;
    int arr[42] = {};
    for (int i = 0; i < 10; i++) {
        cin >> a;
        arr[a % 42]++;
    }
    int cnt = 0;
    for (int i : arr) {
        if (i > 0)
            cnt++;
    }
    cout << cnt;
    return 0;
}