#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;

int l, w;
char map[51][51];
int res = 0;
vector<pair<int, int>> land;
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int check[51][51];
void bfs(int y, int x) {
    memset(check, 0, sizeof(check));
    queue<pair<int, int>> q;
    q.push({ y,x });
    check[y][x] = 1;
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny < l && ny >= 0 && nx < w && nx >= 0) {
                if (check[ny][nx] == 0) {
                    if (map[ny][nx] == 'L') {
                        check[ny][nx] = check[y][x] + 1;
                        q.push({ ny,nx });
                    }
                }
            }
        }
    }
    int temp = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < w; j++) {
            if (temp < check[i][j]) temp = check[i][j];
        }
    }
    res = max(res, temp);
}

int main() {
    cin >> l >> w;
    for (int i = 0; i < l; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < w; j++) {
            map[i][j] = s[j];
            if (map[i][j] == 'L') land.push_back({ i,j });
        }
    }
    for (int i = 0; i < land.size(); i++) {
        bfs(land[i].first, land[i].second);
    }
    cout << res-1;
    return 0;
}