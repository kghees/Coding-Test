#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int n, m;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int miro[101][101];
int check[101][101];
void bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({ x,y });
    check[x][y] = 1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < n && nx >= 0 && ny < m && ny >= 0) {
                if (miro[nx][ny] == 1 && check[nx][ny] == 0) {
                    check[nx][ny] == 1;
                    miro[nx][ny] = miro[x][y] + 1;
                    q.push({ nx,ny });
                }
            }
        }
    }
}
int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            miro[i][j] = s[j] - '0';
        }
    }
    bfs(0, 0);
    cout << miro[n - 1][m - 1];
    return 0;
}