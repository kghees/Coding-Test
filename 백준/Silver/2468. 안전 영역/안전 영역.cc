#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;

int n;
int map[101][101];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int res = 1;
bool check[101][101] = { false };

void bfs(int x, int y, int temp) {
    queue<pair<int, int>>q;
    q.push({ x,y });
    check[x][y] = true;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < n && nx >= 0 && ny < n && ny >= 0 && !check[nx][ny]) {
                if (map[nx][ny] > temp) {
                    check[nx][ny] = true;
                    q.push({ nx,ny });
                }
            }
        }
    }
}
int main() {
    cin >> n;
    int a = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
            a = max(map[i][j], a);
        }
    }
    for (int k = 0; k <= a; k++) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] > k && !check[i][j]) {
                    bfs(i, j, k);
                    cnt++;
                }
            }
            res = max(cnt, res);
        }
        memset(check, false, sizeof(check));
    }
    cout << res;
    return 0;
}