#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int n,res = 0;
int number[25][25];
int dat[25] = { 0 };
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };

int bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({ x,y });
    number[x][y] = 0;
    int cnt = 1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < n && nx >= 0 && ny < n && ny >= 0) {
                if (number[nx][ny] == 1) {
                    cnt++;
                    number[nx][ny] = 0;
                    q.push({ nx,ny });
                }
            }
        }
    }
    return cnt;
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            number[i][j] = s[j] - '0';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (number[i][j] == 1) {
                dat[res] = bfs(i, j);
                res++;
            }
        }
    }
    cout << res << '\n';
    sort(dat, dat + res);
    for (int i = 0; i < res; i++) {
        cout << dat[i] << '\n';
    }
    return 0;
}
