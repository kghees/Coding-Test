#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int m, n, k;
int map[101][101] = { 0 };
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int bfs(int x, int y) {
    queue<pair<int, int>>q;
    q.push({ x,y });
    int cnt = 1;
    map[x][y] = 1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < m && nx >= 0 && ny < n && ny >= 0) {
                if (map[nx][ny] == 0) {
                    map[nx][ny] = 1;
                    cnt++;
                    q.push({ nx,ny });
                }
            }
        }
    }
    return cnt;
}

int main() {
    cin >> m >> n >> k;
    for (int i = 0; i < k; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        for (int j = b; j < d; j++) {
            for (int l = a; l < c; l++) {
                map[j][l] = 1;
            }
        }
    }
    int res = 0;
    vector<int> dat; 
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 0) {
                int temp = bfs(i, j);
                dat.push_back(temp);
                res++;
            }
        }
    }
    sort(dat.begin(), dat.end()); 
    cout << res << '\n';
    for (int i = 0; i < res; i++) {
        cout << dat[i] << " ";
    }
    return 0;
}
