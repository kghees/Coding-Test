#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

struct Point {
    int y, x, sec;
};

int t, n;
int map[16][16];
bool visited[16][16];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int sy, sx, ey, ex;

void init() {
    memset(map, 0, sizeof(map));
    memset(visited, false, sizeof(visited));
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
    cin >> sy >> sx >> ey >> ex;
}

int bfs() {
    queue<Point> q;
    q.push({ sy,sx ,0});
    visited[sy][sx] = true;

    while (!q.empty()) {
        Point now = q.front();
        q.pop();

        int y = now.y;
        int x = now.x;
        int sec = now.sec;
        if (y == ey && x == ex) return sec;
        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= n || ny < 0 || nx >= n || nx < 0) continue;
            if (map[ny][nx] == 1 || visited[ny][nx]) continue;
            if (map[ny][nx] == 2 && sec % 3 == 2 || map[ny][nx] == 0) {
                visited[ny][nx] = true;
                q.push({ ny,nx,sec + 1 });
            }
            else q.push({ y,x,sec + 1 });
        }
    }
    return -1;
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        int res = bfs();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}