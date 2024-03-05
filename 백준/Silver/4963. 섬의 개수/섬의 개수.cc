#include <iostream>
#include <cstring>
using namespace std;

int w, h;
int map[51][51];
int dy[8] = {0,0,-1,1,-1,-1,1,1};
int dx[8] = {-1,1,0,0,-1,1,-1,1};

void dfs(int y, int x) {
    map[y][x] = 0;

    for (int i = 0; i < 8; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < h && ny >= 0 && nx < w && nx >= 0) {
            if (map[ny][nx] == 1) {
                map[ny][nx] = 0;
                dfs(ny, nx);
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
        int res = 0; //섬의 개수
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] == 1) {
                    dfs(i, j); //1일때 마다 돌고 모두 1인거 모두 0으로 처리해주면 최종 섬의 개수 나옴
                    res++;
                }
            }
        }
        cout << res << '\n';
    }
}
