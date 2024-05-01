#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
struct stone {
    int y, x;
    int cost;
};

int t, n, w, h;
int map[16][13];
int copy_map[16][13];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int res;

void init() {
    memset(map, 0, sizeof(map));
    memset(copy_map, 0, sizeof(copy_map));
    res = 1e9;
}

void input() {
    cin >> n >> w >> h;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> map[i][j];
            copy_map[i][j] = map[i][j];
        }
    }
}

void breaking(int y, int x) {
    queue<stone> q;
    q.push({ y,x,map[y][x] });

    while (!q.empty()) {
        stone now = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            for (int i = 0; i < now.cost; i++) {
                int ny = now.y + dy[k] * i;
                int nx = now.x + dx[k] * i;

                if (ny >= h || ny < 0 || nx >= w || nx < 0) continue;
                if (map[ny][nx] != 0 && map[ny][nx] != 1) q.push({ny,nx,map[ny][nx]});
                map[ny][nx] = 0;
            }
        }
    }
}

void make() {
    vector<int> v;
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < h; j++) {
            if (map[j][i] != 0) {
                v.push_back(map[j][i]);
                map[j][i] = 0;
            }
        }
        int temp = v.size();
        for (int j = 0; j < temp; j++) {
            map[h - j - 1][i] = v[v.size()-1];
            v.pop_back();
        }
        v.clear();
    }
}

void dfs(int cnt) {
    if (cnt == n) {
        int temp = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] != 0) temp++;
            }
        }
        res = min(res, temp);
        return;
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (map[i][j] != 0) {
                if (i == 0 || map[i - 1][j] == 0) {
                    int temp_map[16][13];
                    memcpy(temp_map, map, sizeof(map));
                    if (map[i][j] == 1) map[i][j] = 0;
                    else {
                        breaking(i, j);
                        make();
                    }
                    
                    dfs(cnt + 1);
                    memcpy(map, temp_map, sizeof(map));
                }
            }
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        dfs(0);
        if(res == 1e9) cout << "#" << tc + 1 << " " << 0 << '\n';
        else cout << "#" << tc + 1 << " " << res << '\n';
        
    }
    return 0;
}