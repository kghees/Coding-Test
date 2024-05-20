#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n, m;
int map[1001][1001];
int dat[1001][1001];
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
int res;

void bfs(int y, int x) {
    queue<pair<int, int>> q1;
    queue<pair<int, int>> q2;
    q1.push({ y,x });
    dat[y][x] = 1;

    while (!q1.empty()) {
        int y = q1.front().first;
        int x = q1.front().second;
        q1.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= n || ny < 0 || nx >= m || nx < 0) continue;
            if (dat[ny][nx]) continue;
            dat[ny][nx] = dat[y][x] + 1;
            if (map[ny][nx]) q2.push({ ny,nx });
            else q1.push({ ny,nx });
        }
    }
    res = dat[n - 1][m - 1];

    while (!q2.empty()) {
        int y = q2.front().first;
        int x = q2.front().second;
        q2.pop();
        int next = dat[y][x] + 1;

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= n || ny < 0 || nx >= m || nx < 0) continue;
            if (map[ny][nx]) continue;

            if (!dat[ny][nx] || next < dat[ny][nx]) {
                dat[ny][nx] = next;
                q2.push({ ny,nx });
            }
        }
    }
    if (!res || res > dat[n - 1][m - 1]) {
        res = dat[n - 1][m - 1];
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            map[i][j] = s[j] - '0';
        }
    }
    bfs(0, 0);

    if (!res) cout << -1;
    else cout << res;
    return 0;
}