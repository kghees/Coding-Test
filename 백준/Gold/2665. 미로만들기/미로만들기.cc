#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n;
int map[51][51];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int check[51][51];

void bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({ x,y });
    check[x][y] = 0;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for(int k = 0; k < 4; k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < n && nx >= 0 && ny < n && ny >= 0) {
                if (map[nx][ny] == 1) {
                    if (check[nx][ny] > check[x][y]) {
                        check[nx][ny] = check[x][y];
                        q.push({ nx,ny });
                    }
                }
                else {
                    if (check[nx][ny] > check[x][y]) {
                        check[nx][ny] = check[x][y] + 1;
                        q.push({ nx,ny });
                    }
                }
            }
        }
    }
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            map[i][j] = s[j] - '0';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            check[i][j] = 21e8;
        }
    }
    bfs(0, 0);
    cout << check[n - 1][n - 1];
    return 0;
}