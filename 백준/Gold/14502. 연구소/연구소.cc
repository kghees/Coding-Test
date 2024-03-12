#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;

int n, m;
int a[8][8];
vector<pair<int,int>> virusList;
vector<pair<int,int>> wallList;
int ret = 0;
int visited[8][8];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };

void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({ y,x });

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= n || ny < 0 || nx >= m || nx < 0) continue;
            if (visited[ny][nx] || a[ny][nx] == 1) continue;
            visited[ny][nx] = 1;
            q.push({ ny,nx });
        }
    }
    return;
}

int solve() {
    memset(visited, 0, sizeof(visited));
    for (pair<int, int> i : virusList) {
        visited[i.first][i.second] = 1;
        bfs(i.first, i.second);
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 0 && !visited[i][j]) cnt++;
        }
    }
    return cnt;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
            if (a[i][j] == 2) virusList.push_back({ i,j });
            if (a[i][j] == 0) wallList.push_back({ i,j });
        }
    }
    for (int i = 0; i < wallList.size(); i++) {
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < j; k++) {
                a[wallList[i].first][wallList[i].second] = 1;
                a[wallList[j].first][wallList[j].second] = 1;
                a[wallList[k].first][wallList[k].second] = 1;
                ret = max(ret, solve());
                a[wallList[i].first][wallList[i].second] = 0;
                a[wallList[j].first][wallList[j].second] = 0;
                a[wallList[k].first][wallList[k].second] = 0;
            }
        }
    }
    cout << ret;
}
