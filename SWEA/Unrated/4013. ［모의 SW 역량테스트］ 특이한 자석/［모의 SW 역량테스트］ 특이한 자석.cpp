#include <iostream>
#include <cmath>
using namespace std;

int t, k;
int gear[4][8];

void rotate(int x, int d) {
    if (d == 1) {
        int temp = gear[x][7];
        for (int i = 7; i > 0; i--) {
            gear[x][i] = gear[x][i - 1];
        }
        gear[x][0] = temp;
    }
    else {
        int temp = gear[x][0];
        for (int i = 0; i < 7; i++) {
            gear[x][i] = gear[x][i + 1];
        }
        gear[x][7] = temp;
    }
}

void right(int x, int d) {
    if (x > 2) return;
    if (gear[x][2] != gear[x+1][6]) {
        right(x + 1, -d);
        rotate(x+1, -d);
    }
}

void left(int x, int d) {
    if (x < 1) return;
    if (gear[x][6] != gear[x - 1][2]) {
        left(x - 1, -d);
        rotate(x - 1, -d);
    }
}
int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> k;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 8; j++) {
                cin >> gear[i][j];
            }
        }
        for (int j = 0; j < k; j++) {
            int a, b;
            cin >> a >> b;
            right(a - 1, b);
            left(a - 1, b);
            rotate(a - 1, b);
        }
        int res = 0;
        for (int j = 0; j < 4; j++) {
            if (gear[j][0] != 0) res += pow(2, j);
        }
        cout << "#" << i + 1 << " " << res << '\n';
    }
    return 0;
}