#include <iostream>
#include <algorithm>
#include <vector>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int r, c;
int jy, jx;
int fire_check[1001][1001];
int person_check[1001][1001];
char map[1001][1001];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int res = 0;


void bfs2(int y, int x) {
    queue<pair<int, int>> q1;
    q1.push({ y,x });
    person_check[y][x] = 1;

    while (!q1.empty()) {
        int y = q1.front().first;
        int x = q1.front().second;
        q1.pop();

        if (y == r - 1 || y == 0 || x == c - 1 || x == 0) {
            res = person_check[y][x];
            return;
        }

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= r || ny < 0 || nx >= c || nx < 0) continue;
            if (person_check[ny][nx] || map[ny][nx] == '#') continue;
            if (fire_check[ny][nx] <= person_check[y][x] + 1) continue;
            person_check[ny][nx] = person_check[y][x] + 1;
            q1.push({ ny,nx });
        }
    }
}

int main() {
    cin >> r >> c;
    for (int i = 0; i < 1001; i++) {
        for (int j = 0; j < 1001; j++) {
            fire_check[i][j] = 1001;
        }
    }
    queue<pair<int, int>> q;
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++) {
            map[i][j] = s[j];
            if (s[j] == 'F') {
                fire_check[i][j] = 1;
                q.push({ i,j });
            }
            else if (s[j] == 'J') {
                jy = i;
                jx = j;
            }
        }
    }
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= r || ny < 0 || nx >= c || nx < 0) continue;
            if (fire_check[ny][nx] != 1001 || map[ny][nx] == '#') continue;
            fire_check[ny][nx] = fire_check[y][x] + 1;
            q.push({ ny,nx });
        }
    }
    bfs2(jy, jx);
    if (res != 0) cout << res;
    else cout << "IMPOSSIBLE";
    return 0;
}