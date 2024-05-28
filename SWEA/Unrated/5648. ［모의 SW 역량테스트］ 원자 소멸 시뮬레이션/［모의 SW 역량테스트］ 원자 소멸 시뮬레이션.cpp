#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
struct node {
    int x, y;
    int d;
    int cost;
    bool live;
};

int t, n;
int map[4001][4001]; //0.5초에 만나는 거 때문에 맵도 2배 때리기
int res;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 }; //상하좌우
vector<node> v;


void init() {
    memset(map, 0, sizeof(map));
    res = 0;
    v.clear();
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        //0.5초에 만나는거 떄문에 좌표 두배 때리기
        a = (a + 1000) * 2;
        b = (b + 1000) * 2;
        v.push_back({ a,b,c,d,true });
        map[a][b] = 1;
    }
}

bool check() {
    //살아 있는게 2개이상있으면 충돌할 가능성 있음
    int cnt = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i].live) cnt++;
        if (cnt >= 2) return true;
    }
    return false;
}

void moving() {
    while (1) {
        if (!check()) break;
        for (int i = 0; i < v.size(); i++) {
            if (!v[i].live) continue; //소멸된 거 continue
            //방향에 맞게 이동
            int nx = v[i].x + dx[v[i].d];
            int ny = v[i].y + dy[v[i].d];
            //범위를 벗어나면 소멸 시켜주고 계속 진행
            if (ny > 4000 || ny < 0 || nx > 4000 || nx < 0) {
                map[v[i].x][v[i].y] = 0;
                //v[i].y = -1, v[i].x = -1;
                v[i].live = false;
                continue;
            }
            //범위 안에 있으면 방향 맞게 이동 시켜주기
            map[v[i].x][v[i].y] = 0;
            v[i].y = ny, v[i].x = nx;
            map[nx][ny] += 1;

        }
        //원자들 다 이동 후 충돌 했는지 검사
        for (int i = 0; i < v.size(); i++) {
            if (!v[i].live) continue;
            //2이상이라면 충돌
            if (map[v[i].x][v[i].y] >= 2) {
                int temp = 0;
                for (int j = 0; j < v.size(); j++) {
                    if (i == j) continue;
                    if (!v[j].live) continue;
                    //좌표가 같은 것에 대해서 처리
                    if (v[i].y == v[j].y && v[i].x == v[j].x) {
                        temp += v[j].cost;
                        v[j].live = false;
                        //v[j].y = -1, v[j].x = -1;
                    }
                }
                //현재 원자에 대해서도 처리 
                map[v[i].x][v[i].y] = 0;
                //v[i].y = -1, v[i].x = -1;
                v[i].live = false;
                temp += v[i].cost;
                //최종 값에 에너지 더해주기
                res += temp;
            }
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        moving();
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}
