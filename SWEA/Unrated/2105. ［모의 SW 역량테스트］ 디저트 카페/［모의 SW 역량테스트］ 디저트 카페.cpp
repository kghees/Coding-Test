#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int t, n;
int map[21][21];
int dat[101];
int dy[4] = { 1,1,-1,-1 }; // 우하 -> 좌하 -> 좌상 -> 우상
int dx[4] = { 1,-1,-1,1 };
int res;


void init() {
    memset(map, 0, sizeof(map));
    memset(dat, 0, sizeof(dat));
    res = -1;
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
}

void eat(int cnt, int y, int x, int sy, int sx, int dir) {
    if (dir == 4) return;

    if (y == sy && x == sx) {
        res = max(cnt, res);
        return;
    }
    if (y >= n || y < 0 || x >= n || x < 0) return;
    if (dat[map[y][x]] == 0) {
        dat[map[y][x]] = 1;
        eat(cnt + 1, y + dy[dir], x + dx[dir], sy, sx, dir);
        eat(cnt + 1, y + dy[dir + 1], x + dx[dir + 1], sy, sx, dir + 1);
        dat[map[y][x]] = 0;
    }
    else return;
}

void cafe() {
    //n-2보다 작아야 사각형 만들어지고
    for (int i = 0; i < n-2; i++) {
        //1보다 크고 n-1보다 작아야 사각형 만들어짐
        for (int j = 1; j < n-1; j++) {
            dat[map[i][j]] = 1;
            eat(1, i+1, j+1, i, j, 0);
            dat[map[i][j]] = 0;
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        cafe();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}