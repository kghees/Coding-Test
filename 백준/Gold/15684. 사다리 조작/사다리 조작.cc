#include <iostream>
#include <algorithm>
using namespace std;

int n, m, h;
int res = 1e9;
int map[31][31];

bool check() {
    for (int i = 1; i <= n; i++) {
        int temp = i; //현재 i번째 사다리
        for (int j = 1; j <= h; j++) {
            if (map[j][temp]) temp++; //오른쪽 이동
            else if (map[j][temp - 1]) temp--; //왼쪽 이동
        }
        if (temp != i) return false; //끝에 다달랐을 때 다르면 false
    }
    return true; //제대로 다 왔으면 true
}

void dfs(int idx, int lev) {
    //3개 초과거나 이미 최소를 찾았으면 return
    if (lev > 3 || lev >= res) return;
    //i번째로 가는지 확인되면 최소 값 비교
    if (check()) {
        res = min(res, lev);
        return;
    }
    //중복 방지위해 idx부터 시작
    for (int i = idx; i <= h; i++) {
        for (int j = 1; j <= n; j++) {
            //접하면 안되므로 현재좌표 및 양 옆 좌표 확인
            if (map[i][j] || map[i][j+1] || map[i][j-1]) continue;
            map[i][j] = 1;
            dfs(i, lev + 1);
            map[i][j] = 0;
        }
    }
}

int main() {
    cin >> n >> m >> h;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
    }
    //중복 방지 위한 인덱스, 현재 놓은 사다리 개수
    dfs(0, 0);

    if (res == 1e9) cout << -1;
    else cout << res;
    return 0;
}