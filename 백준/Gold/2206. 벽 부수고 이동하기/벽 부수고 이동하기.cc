#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct wall {
    int y, x;
    int chance;
};

int n, m;
int map[1001][1001];
int dat[1001][1001][2];
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
int res;

int bfs() {
    queue<wall> q;
    q.push({ 0,0,0 }); //y,x좌표 및 벽 부순 여부
    dat[0][0][0] = 1; //시작 점 1

    while (!q.empty()) {
        wall now = q.front();
        q.pop();
        //좌표 도달했으면 값 return
        if (now.y == n - 1 && now.x == m - 1) return dat[now.y][now.x][now.chance];

        for (int k = 0; k < 4; k++) {
            int ny = now.y + dy[k];
            int nx = now.x + dx[k];
            //범위 안에 있고 
            if (ny < n && ny >= 0 && nx < m && nx >= 0) {
                //벽이 없고 아직 방문하지 않은 경우
                if (!map[ny][nx] && !dat[ny][nx][now.chance]) {
                    dat[ny][nx][now.chance] = dat[now.y][now.x][now.chance] + 1;
                    q.push({ ny,nx,now.chance });
                }
                //벽인데 아직 벽 안부쉈다면
                if (map[ny][nx] && now.chance == 0) {
                    dat[ny][nx][now.chance + 1] = dat[now.y][now.x][now.chance] + 1;
                    q.push({ ny,nx, now.chance + 1 });
                }
            }

        }
    }
    //못갔으면 -1 return
    return -1;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            map[i][j] = s[j] - '0';
        }
    }
    cout << bfs();
    return 0;
}