#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int n, m;
int map[51][51];
vector<pair<int, int>> home;
vector<pair<int, int>> chicken;
int res = 1e9;
bool visited[13] = { false };

void calc() {
    int temp[51][51];
    memset(temp, 10000, sizeof(temp));
    for (int i = 0; i < chicken.size(); i++) {
        for (int j = 0; j < home.size(); j++) {
            if (visited[i]) {
                int a = abs(home[j].first - chicken[i].first) + abs(home[j].second - chicken[i].second);
                temp[home[j].first][home[j].second] = min(temp[home[j].first][home[j].second], a);
            }
        }
    }
    int check = 0;
    for (int i = 0; i < home.size(); i++) {
        check += temp[home[i].first][home[i].second];
    }
    res = min(check, res);
}

void dfs(int idx, int cnt) {
    if (cnt == m) {
        calc();
        return;
    }
    for (int i = idx; i < chicken.size(); i++) {
        if (visited[i]) continue;
        visited[i] = true;
        dfs(i+1,cnt + 1);
        visited[i] = false;
    }
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1) home.push_back({ i,j });
            if (map[i][j] == 2) chicken.push_back({ i,j });
        }
    }
    dfs(0,0);
    cout << res;
    return 0;
}