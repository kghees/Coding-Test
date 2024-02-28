#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int t;
int dy[8] = {0,0,-1,1,-1,-1,1,1};
int dx[8] = {-1,1,0,0,-1,1,-1,1};
int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        int map[8][8];
        memset(map, 0, sizeof(map));
        int n, m;
        cin >> n >> m;
        map[n / 2 - 1][n / 2 - 1] = 2;
        map[n / 2 - 1][n / 2] = 1;
        map[n / 2][n / 2 - 1] = 1;
        map[n / 2][n / 2] = 2;
        for (int j = 0; j < m; j++) {
            int x, y, d;
            cin >> x >> y >> d;
            x -= 1;
            y -= 1;
            vector<pair<int, int>> arr;
            for (int k = 0; k < 8; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                while (true) {
                    if (nx >= n || nx < 0 || ny >= n || ny < 0) {
                        arr.clear();
                        break;
                    }
                    if (map[nx][ny] == 0) {
                        arr.clear();
                        break;
                    }
                    if (map[nx][ny] == d) break;
                    else {
                        arr.push_back({ nx,ny });
                    }
                    nx += dx[k];
                    ny += dy[k];
                }
                for (auto p : arr) {
                    map[p.first][p.second] = d;
                }
                map[x][y] = d;
            }
        }
        int b = 0, w = 0;
        for (int l = 0; l < n; l++) {
            for (int k = 0; k < n; k++) {
                if (map[l][k] == 1) b++;
                else if (map[l][k] == 2) w++;
            }
        }
        cout << "#" << i + 1 << " " << b << " " << w << '\n';
    }
    return 0;
}