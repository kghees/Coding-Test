#include <iostream>
#include <queue>
#include <vector>
#include <cmath> 
#include <cstring> 
using namespace std;

int n, l, r;
int map[50][50]; 
bool visited[50][50];
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 }; 


bool bfs(int x, int y) {
    queue<pair<int, int>> q;
    vector<pair<int, int>> united; 
    int temp = 0; 
    int cnt = 0; 

    q.push({ x, y });
    visited[x][y] = true;
    united.push_back({ x, y });
    temp += map[x][y];
    cnt++;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

            if (!visited[nx][ny]) {
                if (abs(map[x][y] - map[nx][ny]) >= l && abs(map[x][y] - map[nx][ny]) <= r) {
                    q.push({ nx, ny });
                    visited[nx][ny] = true;
                    united.push_back({ nx, ny });
                    temp += map[nx][ny];
                    cnt++;
                }
            }
        }
    }

    if (cnt > 1) { 
        int avg = temp / cnt;
        for (auto i : united) {
            map[i.first][i.second] = avg;
        }
        return true; 
    }
    else {
        return false; 
    }
}



int main() {
    cin >> n >> l >> r;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }

    int res = 0;
    bool possible = true;

    while (possible) {
        possible = false;
        memset(visited, false, sizeof(visited));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if (bfs(i, j)) {
                        possible = true;
                    }
                }
            }
        }

        if (possible) res++;
    }
    cout << res;

    return 0;
}
