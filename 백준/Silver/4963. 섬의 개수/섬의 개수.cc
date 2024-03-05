#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int w, h;
int map[51][51];
int dy[8] = {0,0,-1,1,-1,-1,1,1};
int dx[8] = {-1,1,0,0,-1,1,-1,1};

void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({ y,x });
    map[y][x] = 0;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int i = 0; i < 8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < h && ny >= 0 && nx < w && nx >= 0) {
                if (map[ny][nx] == 1) {
                    map[ny][nx] = 0;
                    q.push({ ny,nx });
                }
            }
        }
    }
}

int main(){
    while (true) {
        cin >> w >> h;
        memset(map, 0, sizeof(map));
        if (w == 0 && h == 0) break;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                cin >> map[i][j];
            }
        }
        int res = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] == 1) {
                    bfs(i, j);
                    res++;
                }
            }
        }
        cout << res << '\n';
    }
    
}
