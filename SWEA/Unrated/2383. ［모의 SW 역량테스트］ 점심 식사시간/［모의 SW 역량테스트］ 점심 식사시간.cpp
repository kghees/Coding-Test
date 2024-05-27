#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;
struct node {
    int y, x;
    int cost;
};

int t, n;
int map[11][11];
vector<node> st;
vector<pair<int, int>> human;
int res;

void init() {
    memset(map, 0, sizeof(map));
    st.clear();
    human.clear();
    res = 1e9;
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1) human.push_back({ i,j });
            else if (map[i][j] > 1) st.push_back({ i,j , map[i][j]});
        }
    }
}

int calc(int idx, vector<int> v) {
    int sttime = st[idx].cost; //각 계단 내려가는데 걸리는 시간
    int wait[3] = { 0 };
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++) {
        int d = i % 3; //wait배열에서 확인해야 할 인덱스
        int k = v[i]; //각 사람들이 계단까지 오는데 걸리는 시간
        //계단 도착하기 전에 wait배열에 사람이 없다면
        if (wait[d] < k) {
            wait[d] = k + sttime; //계단 까지 오는데 걸리는 시간 + 내려가는데 걸리는 시간
        }
        //계단 도착했는데 사람이 이미 있다면
        else {
            //앞사람 탈출 시간 + 내려가는 시간
            wait[d] += sttime;
        }
    }
    //모든 사람이 빠져나가는데 걸리는 시간
    return max({ wait[0],wait[1],wait[2] });
}

void dfs(int lev, vector<int> &v1, vector<int>&v2) {
    if (lev == human.size()) {
        int temp1 = calc(0, v1); //0 1번계단
        int temp2 = calc(1, v2); //1 2번계단
        int ans = max(temp1, temp2);
        res = min(ans, res);
        return;
    }

    //계단까지 걸리는 시간
    int hy = human[lev].first;
    int hx = human[lev].second;
    int s1y = st[0].y;
    int s1x = st[0].x;
    int s2y = st[1].y;
    int s2x = st[1].x;

    int d1 = abs(s1y - hy) + abs(s1x - hx);
    int d2 = abs(s2y - hy) + abs(s2x - hx);

    v1.push_back(d1);
    dfs(lev + 1, v1, v2); //1번 계단 이용
    v1.pop_back();

    v2.push_back(d2);
    dfs(lev + 1, v1, v2); //2번 계단 이용
    v2.pop_back();
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        vector<int> v1, v2;
        dfs(0,v1,v2);

        cout << "#" << tc + 1  << " " << res + 1 << '\n';
    }
    return 0;
}