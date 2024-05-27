#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int t, n;
int map[21][21];
int dat[101];
int dy[4] = { 1,1,-1,-1 }; //우하 좌하 좌상 우상
int dx[4] = { 1,-1,-1,1 };
int res;

void init() {
    memset(map, 0, sizeof(map));
    memset(dat, 0,sizeof(dat));
    res = -1;
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++){
            cin >> map[i][j];
        }
    }
}

void dfs(int ey, int ex, int y, int x, int cnt, int dir) {
    if (dir == 4) return; //방향이 3을 넘어가면 안됨
    //출발지 좌표와 같아지면 최대값 비교
    if (ey == y && ex == x) {
        res = max(res, cnt);
        return;
    }
    //범위 넘어가면 return
    if (y >= n || y < 0 || x >= n || x < 0) return;
    //먹지 않은 디저트라면
    if (!dat[map[y][x]]) {
        dat[map[y][x]] = 1;//해당 디저트 먹어주고
        //같은 방향으로 계속 탐색
        dfs(ey, ex, y + dy[dir], x + dx[dir], cnt + 1, dir);
        //다른 방향으로 탐색
        dfs(ey, ex, y + dy[dir + 1], x + dx[dir + 1], cnt + 1, dir + 1);
        dat[map[y][x]] = 0; //다른 탐색을 위해 먹은거 취소
    }
    else return; //먹은 디저트라면 return
}

void cafe() {
    //0이상 n-2미만이어야 대각선으로 사각형이 만들어짐
    for (int i = 0; i < n - 2; i++) {
        //1이상 n-1미만이어야 대각선으로 사각형이 만들어짐
        for (int j = 1; j < n - 1; j++) {
            dat[map[i][j]] = 1; //해당 좌표 디저트 먹어주고
            //출발지 좌표, 대각선 우하로 이동한 좌표,현재 먹은 디저트 갯수, 현재 방향
            dfs(i, j, i+1, j+1, 1, 0);
            dat[map[i][j]] = 0;//다른 탐색을 위해 먹은거 취소
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        cafe();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}