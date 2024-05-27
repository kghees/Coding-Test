#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int t, n;
char map[301][301];
bool visited[301][301];
vector<pair<int, int>> v;
int res;
int dy[8] = { -1,-1,-1,0,1,1,0,1 };
int dx[8] = { -1,0,1,-1,-1,0,1,1 };

void init() {
    memset(map, ' ', sizeof(map));
    memset(visited, false, sizeof(visited));
    res = 0;
    v.clear();
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            map[i][j] = s[j];
            //지뢰가 없는 칸들만 탐색하기 위해 따로 좌표 넣어주기
            if (map[i][j] == '.') v.push_back({ i,j });
        }
    }
}
//8방향에 대해서 지뢰가 없는 칸인지 확인
bool check(int y, int x) {
    for (int k = 0; k < 8; k++) {
        int ny = y + dy[k];
        int nx = x + dx[k];

        if (ny < n && ny >= 0 && nx < n && nx >= 0) {
            if (map[ny][nx] == '*')return false;
        }
    }
    return true;
}
//연쇄적으로 8방향에 대해서 없는 칸인지 찾기 위함
void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({ y,x });
    visited[y][x] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 8; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];
           //범위 안에 있고
            if (ny < n && ny >= 0 && nx < n && nx >= 0) {
                if (!visited[ny][nx]) { //방문하지 않았다면
                    visited[ny][nx] = true; //방문 체크
                    //8방향에 대해서 지뢰가 없다면 연쇄적으로 탐색이 가능하니
                    //q에 넣어주기
                    if (check(ny, nx)) q.push({ ny,nx });
                }
            }
        }
    }
}

void search() {
    // '.'으 갯수 만큼 탐색
    for (int i = 0; i < v.size(); i++) {
        //이미 방문했다면 continue
        if (visited[v[i].first][v[i].second]) continue;
        //8방향에 대해서 지뢰가 없는 칸인지 확인
        if (check(v[i].first, v[i].second)) {
            bfs(v[i].first, v[i].second);
            res++;
        }
    }
    //주변에 지뢰가 있어서 못들어간 것들에 대해서도 세주기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == '.' && !visited[i][j]) res++;
        }
    }
    
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        search();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}