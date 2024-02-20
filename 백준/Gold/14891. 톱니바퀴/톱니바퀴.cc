#include <iostream>
#include <algorithm>
#include<cmath>
using namespace std;
int gear[4][8];

void run(int g,int d) { 
    if (d == 1) {
        int temp = gear[g][7];
        for (int i = 7; i > 0; i--) {
            gear[g][i] = gear[g][i - 1];
        }
        gear[g][0] = temp;
    }
    else {
        int temp = gear[g][0];
        for (int i = 0; i < 7; i++) {
            gear[g][i] = gear[g][i+1];
        }
        gear[g][7] = temp;
    }
}

void right(int x, int d) {
    if (x > 2) return;
    if (gear[x][2] != gear[x + 1][6]) {
        right(x + 1, -d);
        run(x+1, -d);
    }
    return;
}

void left(int x, int d) {
    if (x < 1) return;
    if (gear[x][6] != gear[x - 1][2]) {
        left(x - 1, -d);
        run(x - 1, -d);
    }
    return;
}
int main() {
    for (int i = 0; i < 4; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            gear[i][j] = s[j] - '0';
        }
    }
    int k;
    cin >> k;
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        right(a - 1, b);
        left(a - 1, b);
        run(a - 1, b);
    }
    int res = 0;
    for (int i = 0; i < 4; i++) {
        if (gear[i][0]) res += pow(2, i);
    }
    cout << res;
    return 0;
}