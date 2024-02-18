#include <iostream>
using namespace std;

int map[101][101];
int n, l;
int res = 0;

void row(int x, int y, int cnt) {
    int cur = map[x][y];
    int next = map[x][y + 1];
    if (y + 1 == n) {
        res++;
        return;
    }
    if (cur == next) {
        row(x, y + 1, cnt + 1);
    }
    else if (cur + 1 == next) {
        if (cnt >= l)
            row(x, y + 1, 1);
        return;
    }
    else if (cur == next + 1) {
        if (y + l < n) {
            for (int i = y + 1; i < y + 1 + l; i++) {
                if (next != map[x][i]) return;
            }
            row(x, y + l, 0);
        }
    }
}

void col(int x, int y, int cnt) {
    int cur = map[x][y];
    int next = map[x + 1][y];
    if (x + 1 == n) {
        res++;
        return;
    }
    if (cur == next) {
        col(x + 1, y, cnt + 1);
    }
    else if (cur + 1 == next) {
        if (cnt >= l)
            col(x + 1, y, 1);
        return;
    }
    else if (cur == next + 1) {
        if (x + l < n) {
            for (int i = x + 1; i < x + 1 + l; i++) {
                if (next != map[i][y]) return;
            }
            col(x + l, y, 0);
        }
    }
}

int main() {
    cin >> n >> l;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        row(i, 0, 1);
        col(0, i, 1);
    }
    cout << res;
    return 0;
}