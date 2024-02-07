#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int t, m, n,k;
int cabbage[51][51];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };

void dfs(int x, int y) {
    cabbage[x][y] = 0;
    for (int l = 0; l < 4; l++) {
        int nx = x + dx[l];
        int ny = y + dy[l];
        if (nx < m && nx >= 0 && ny < n && ny >= 0) {
            if (cabbage[nx][ny] == 1) {
                dfs(nx, ny);
            }
        }
    }
}

void init() {
    memset(cabbage, 0, sizeof(cabbage));
}

int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> m >> n >> k;
        init();
        for (int i = 0; i < k; i++) {
            int a, b;
            cin >> a >> b;
            cabbage[a][b] = 1;
        }
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (cabbage[i][j] == 1) {
                    dfs(i, j);
                    res++;
                }
            }
        }
        cout << res << '\n';
    }
    return 0;
}
