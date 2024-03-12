#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

int n, m;
int map[8][8];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int res = 0;
int copymap[8][8];
bool visit[8][8] = { false };

void copy(int copymap[8][8], int map[8][8]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            copymap[i][j] = map[i][j];
        }
    }

}


void bfs() {
    int check[8][8];
    copy(check, copymap);
    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (check[i][j] == 2) {
                q.push({ i,j });
            }
        }
    }
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];
            if (ny >= n || ny < 0 || nx >= m || nx < 0) continue;
            if (check[ny][nx] == 0) {
                check[ny][nx] = 2;
                q.push({ ny,nx });
            }
        }
    }
    int temp = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (check[i][j] == 0) temp++;
        }
    }
    res = max(res, temp);
}

void dfs(int cnt) {
    if (cnt == 3) {
        bfs();
        return;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (copymap[i][j] == 0) {
                copymap[i][j] = 1;
                dfs(cnt+1);
                copymap[i][j] = 0;
            }
        }
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 0) {
                memset(visit, false, sizeof(visit));
                copy(copymap, map);
                copymap[i][j] = 1;
                dfs(1);
                copymap[i][j] = 0;
            }
        }
    }
    cout << res;
    return 0;
}

