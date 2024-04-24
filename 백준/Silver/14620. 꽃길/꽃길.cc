#include <iostream>
#include <algorithm>
using namespace std;

int n;
int map[11][11];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
bool visited[11][11] = { false };
int res = 1e9;

int flowers(int y, int x) {
    int temp = 0;
    temp += map[y][x];
    visited[y][x] = true;
    for (int k = 0; k < 4; k++) {
        int ny = y + dy[k];
        int nx = x + dx[k];
        temp += map[ny][nx];
        visited[ny][nx] = true;
    }
    return temp;
}

void turnflowers(int y, int x) {
    visited[y][x] = false;
    for (int k = 0; k < 4; k++) {
        int ny = y + dy[k];
        int nx = x + dx[k];
        visited[ny][nx] = false;
    }
}

bool check(int y, int x) {
    if (visited[y][x]) return false;
    for (int k = 0; k < 4; k++) {
        int ny = y + dy[k];
        int nx = x + dx[k];
        if (ny >= n || ny < 0 || nx >= n || nx < 0 || visited[ny][nx]) return false;
    }
    return true;
}

void dfs(int cnt, int ans) {
    if (cnt == 3) {
        res = min(ans, res);
        return;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (check(i, j)) {
                dfs(cnt + 1, ans + flowers(i, j));
                turnflowers(i, j);
            }
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
    dfs(0, 0);
    cout << res;
    return 0;
}