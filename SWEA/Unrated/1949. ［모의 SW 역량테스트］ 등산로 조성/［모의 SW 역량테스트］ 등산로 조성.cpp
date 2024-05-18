#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t, n, k, res, maxm;
int map[9][9];
bool visited[9][9];
int dy[4] = { 0, 0, -1, 1 };
int dx[4] = { -1, 1, 0, 0 };
vector<pair<int, int>> m;

void init() {
    memset(map, 0, sizeof(map));
    memset(visited, false, sizeof(visited));
    m.clear();
    res = 0;
    maxm = 0;
}

void input() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
            maxm = max(map[i][j], maxm); //가장 높은 봉우리 찾아주기
        }
    }
    //가장 높은 봉우리 좌표 넣어주기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (maxm == map[i][j]) m.push_back({ i,j });
        }
    }
}

bool check(int now, int next, int c) {
    if (!c) return false; //찬스 없으면 X
    if (now  <= next - k) return false; //k만큼 뺐는데도 크거나 같으면 X
    if (now > next) return false; //이미 현재가 더 크면 X
    return true;
}

void dfs(int y, int x, int lev, int chance) {
    res = max(res, lev); //항상 최대 등산로 길이 비교

    //4방향에 대해서
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        //범위 벗어나거나 방문 된 곳 X
        if (ny >= n || ny < 0 || nx >= n || nx < 0) continue;
        if (visited[ny][nx]) continue;
        visited[ny][nx] = true;

        int now = map[y][x];
        int next = map[ny][nx];

        //깎을 경우
        if (check(now, next, chance)) {
            map[ny][nx] = map[y][x] - 1; //1만 빼줘도 갈 수 있음
            dfs(ny, nx, lev + 1, 0); //찬스 없애고 다음으로
            map[ny][nx] = next; // 복구
        }
        //안깎을 경우
        if (now > next) {
            dfs(ny, nx, lev + 1, chance);
        }
        visited[ny][nx] = false;
    }
}

void st() {
    //가장 높은 봉우리 갯수만큼 탐색
    for (int i = 0; i < m.size(); i++) {
        memset(visited, false, sizeof(visited)); //갔다올 때마다 visited배열 초기화
        visited[m[i].first][m[i].second] = true; //현재 봉우리 방문체크
        //현재 봉우리 좌표, 등산로 길이, 깎을 횟수 1회
        dfs(m[i].first, m[i].second, 1, 1);
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        st();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}