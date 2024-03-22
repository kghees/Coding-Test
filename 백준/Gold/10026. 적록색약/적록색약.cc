#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int n;
char map[101][101];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
bool visited[101][101] = { false };
void bfs(int y, int x, char c) {
    queue<pair<int, int>>q;
    q.push({ y,x });
    visited[y][x] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny < n && ny >= 0 && nx < n && nx >= 0) {
                if (!visited[ny][nx] && map[ny][nx] == c) {
                    visited[ny][nx] = true;
                    q.push({ ny,nx });
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
            map[i][j] = s[j];
        }
    }
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                bfs(i, j, map[i][j]);
                res++;
            }
        }
    }
    memset(visited, false, sizeof(visited));
    int res1 = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 'G') map[i][j] = 'R';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                bfs(i, j, map[i][j]);
                res1++;
            }
        }
    }
    cout << res << " " << res1;
    return 0;
}