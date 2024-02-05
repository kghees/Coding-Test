#include <iostream>
using namespace std;

int n, m, r, c, d, cnt = 0;
int robot[50][50];
bool check[50][50] = { false };
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int main() {
    cin >> n >> m >> r >> c >> d;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> robot[i][j];
        }
    }

    check[r][c] = true;
    cnt = 1;

    while (true) {
        int x = 0;

        for (int k = 0; k < 4; k++) {
            d = (d + 3) % 4;
            int nx = r + dx[d];
            int ny = c + dy[d];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || check[nx][ny] || robot[nx][ny] == 1) {
                continue;
            }

            check[nx][ny] = true;
            cnt++;
            r = nx;
            c = ny;
            x = 1;
            break;
        }

        if (x == 0) {
            int nx = r - dx[d];
            int ny = c - dy[d];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || robot[nx][ny] == 1) {
                break;
            }

            r = nx;
            c = ny;
        }
    }

    cout << cnt;

    return 0;
}
