#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, a = 666, cnt = 0;
    cin >> n;
    while (true) {
        if (to_string(a).find("666") != -1)
            cnt++;
        if (cnt == n) {
            cout << a << endl;
            break;
        }
        a++;
    }
    return 0;
}