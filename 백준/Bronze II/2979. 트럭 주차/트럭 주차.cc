#include <iostream>
#include <algorithm>
using namespace std;

int a, b, c;
int dat[101];

int main() {
    cin >> a >> b >> c;
    for (int i = 0; i < 3; i++) {
        int x, y;
        cin >> x >> y;
        for (int i = x; i < y; i++) {
            dat[i]++;
        }
    }
    int res = 0;
    for(int i = 1; i < 101; i++){
        if (dat[i] == 1) {
            res += a;
        }
        else if (dat[i] == 2) {
            res += 2*b;
        }
        else if (dat[i] == 3) {
            res += 3*c;
        }
    }
    cout << res;
    return 0;
}
