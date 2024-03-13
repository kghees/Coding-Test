#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

int n, m;
int map[100][100];
int dy[4] = { -1,0,1,0 };
int dx[4] = { 0,1,0,-1 };
bool check[100][100];
int res = 0;
int cnt = 0;
vector<pair<int, int>> v;

void cheese(int y, int x) {
    queue<pair<int, int>> q;
    q.push({ y,x });
    check[y][x] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        if (map[y][x] == 1) {
            v.push_back({ y,x });
            continue;
        }
        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= n || ny < 0 || nx >= m || nx < 0 || check[ny][nx]) continue;
            check[ny][nx] = true;
            q.push({ ny,nx });
        }
    }
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    }
    while (true) {
        memset(check, false, sizeof(check));
        v.clear();
        cheese(0, 0);
        cnt = v.size();
        for (pair<int, int> i : v) {
            map[i.first][i.second] = 0;
        }
        int temp = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] != 0) temp = 1;
            }
        }
        res++;
        if (!temp) break;
    }
    cout << res << '\n' << cnt;
}
