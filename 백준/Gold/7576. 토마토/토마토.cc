#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int m, n;
int map[1001][1001];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int res = 0;
queue<pair<int, int>> q;


void bfs() {
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny < n && ny >= 0 && nx < m && nx >= 0) {
                if (map[ny][nx] == 0) { 
                    map[ny][nx] = map[y][x] + 1;
                    q.push({ ny,nx });
                }
            }
        }
    }
}

int main() {
    cin >> m >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1) q.push({ i,j });
        }
    }
    bfs();
    int flag = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 0) flag = 1;
            if (res < map[i][j]) res = map[i][j];
        }
    }
    if (!flag) cout << res-1;
    else cout << -1;
    return 0;
}