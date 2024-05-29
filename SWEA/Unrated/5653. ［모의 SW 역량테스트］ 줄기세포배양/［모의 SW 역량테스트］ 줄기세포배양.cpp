#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
struct cell {
    int y, x;
    int cost; //생명력 수치
    int active_time; //활성화 되는 시간
    int die_time; //죽는 시간
};
//우선순위 비교
struct cmp {
    bool operator()(cell a, cell b) {
        return a.cost < b.cost;
    }
};


int t, n, m, k;
int map[651][651];
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
vector<cell> v;
priority_queue<cell, vector<cell>, cmp> pq;

void init() {
    memset(map, 0, sizeof(map));
    v.clear();
}

void input() {
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int a;
            cin >> a;
            map[i + 300][j + 300] = a; //퍼지므로 300 더해서 넣어주기
            if(a != 0) v.push_back({ i + 300, j + 300, a, a, 2 * a });
                
        }
    }
}

void bfs(int now_time) {
    while (!pq.empty()) {
        cell now = pq.top();
        pq.pop();

        for (int i = 0; i < 4; i++) {
            int ny = now.y + dy[i];
            int nx = now.x + dx[i];
            //0인 곳만 퍼질 수 있음
            if (map[ny][nx] == 0) {
                map[ny][nx] = now.cost;
                //v에 넣어주기
                v.push_back({ ny,nx, now.cost, now.cost + now_time + 1, now.cost * 2 + now_time });
            }
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();

        int dead = 0;

        for (int ti = 1; ti < k; ti++) {
            for (int i = 0; i < v.size(); i++) {
                //활성화 된 것들 pq에 넣어주기
                if (v[i].active_time == ti) pq.push(v[i]);
                //죽은 것들 수 세어주기
                if (v[i].die_time == ti) dead++;
            }
            bfs(ti);
        }

        cout << "#" << tc + 1 << " " << v.size() - dead << '\n';
    }
    return 0;
}
