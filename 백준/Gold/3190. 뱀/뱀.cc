#include <iostream>
#include <queue>
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };
using namespace std;
int main() {
    int n, k;
    int bam[102][102] = { 0 };
    bool check[102][102] = { false };
    cin >> n >> k;
    int a, b;
    for (int i = 0; i < k; i++) {
        cin >> a >> b;
        bam[a - 1][b - 1] = 1;
    }
    int cnt = 0;
    char c;

    int d = 0;
    int x = 0, y = 0;
    queue<pair<int, int>> q;
    q.push({x,y});
    int l;
    cin >> l;
    int t1;
    for (int i = 0; i < l; i++) {
        cin >> t1 >> c;

        while (cnt < t1 || i == l - 1) {
            cnt++;
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx < n && nx >= 0 && ny < n && ny >= 0 && !check[nx][ny]) {
                if (bam[nx][ny] == 1) { 
                    bam[nx][ny] = 0; 
                    q.push({nx,ny});
                    check[nx][ny] = true;
                }
                else {
                    q.push({nx,ny});
                    check[nx][ny] = true;
                    check[q.front().first][q.front().second] = false;
                    q.pop();
                }
            }
            else {
                cout << cnt;
                return 0;
            }
            x = nx;
            y = ny;
            if (cnt == t1) {
                if (c == 'D') { 
                    d = (d + 1) % 4;
                }
                else {
                    d = (d + 3) % 4;
                }
            }
        }
    }
    return 0;
}