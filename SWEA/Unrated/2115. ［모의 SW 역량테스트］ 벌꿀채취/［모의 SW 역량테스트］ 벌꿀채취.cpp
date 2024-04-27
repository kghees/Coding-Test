#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t, n, m, c;
int map[11][11];
int res,a,b,maxv;

void init() {
    memset(map, 0, sizeof(map));
    res = 0, a = 0, b = 0, maxv = 0;
}

void input() {
    cin >> n >> m >> c;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
}

void dfs(int cnt, int temp, int sum, int y, int x) {
    if (temp > c) return;

    if (cnt == m) {
        maxv = max(maxv, sum);
        return;
    }

    dfs(cnt + 1, temp + map[y][x + cnt], sum + (map[y][x + cnt] * map[y][x + cnt]), y, x);
    dfs(cnt + 1, temp, sum, y, x);
}

void honey() {
    for (int i1 = 0; i1 < n; i1++) {
        for (int j1 = 0; j1 < n - m + 1; j1++) {
            maxv = 0;
            dfs(0, 0, 0, i1, j1);
            a = maxv;
            for (int i2 = i1; i2 < n; i2++) {
                int nj;
                if (i1 == i2) nj = j1 + m;
                else nj = 0;
                for (int j2 = nj; j2 < n - m + 1; j2++) {
                    maxv = 0;
                    dfs(0, 0, 0, i2, j2);
                    res = max(res, a + maxv);
                }
            }
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        honey();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}