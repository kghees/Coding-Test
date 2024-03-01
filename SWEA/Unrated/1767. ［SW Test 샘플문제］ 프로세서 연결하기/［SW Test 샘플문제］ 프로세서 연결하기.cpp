#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t,n;
int map[13][13];
int maxCorecnt;
int minWirelength ;
int copymap[13][13];

struct Core {
    int y;
    int x;
};
vector<Core> v;

int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };

void init() {
    memset(map, 0, sizeof(map));
    maxCorecnt = 0;
    minWirelength = 1e9;
    v.clear();
}

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
}

void setVector() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 1 && !(i == 0 || i == n - 1 || j == 0 || j == n - 1)) {
                v.push_back({ i,j });
            }
        }
    }
}
void dfs(int idx, int corecnt, int wirelength) {
    //남은 코어 갯수를 전부 더해도 maxCorecnt보다 작을 때
    if ((v.size() + corecnt) - idx < maxCorecnt) return;
    //모든 조합 다 만들어봤으면
    if (idx == v.size()) {
        //최대 연결 가능한 코어 갯수를 찾은 경우
        if (corecnt > maxCorecnt) {
            maxCorecnt = corecnt;
            minWirelength = wirelength;
        }
        // 똑같은 데 더 작은 선을 썼을 경우
        else if (corecnt == maxCorecnt) {
            minWirelength = min(minWirelength, wirelength);
        }
        return;
    }
    for (int i = 0; i < 4; i++) {
        Core now = v[idx];

        bool possible = false;
        //성공 시 :temp 변수 , 실패 시: 원래 변수 보내면 됨
        int tempcorecnt = corecnt;
        int tempwirelength = wirelength;
        int curwirelength = 0; //현재 시도 길이
        //한쪽으로 쭉 직진
        while (true) {
            int ny = now.y + dy[i];
            int nx = now.x + dx[i];
            //넘어가면 전원 연결 된 거임
            if (ny >= n || ny < 0 || nx >= n || nx < 0) {
                tempcorecnt++;
                possible = true;
                break;
            }
            //core 만나거나 전선 만나면 X
            if (copymap[ny][nx] == 1 || copymap[ny][nx] == 2) {
                break;
            }

            now.y = ny; //좌표갱신
            now.x = nx;
            tempwirelength++; //wire길이 늘려주기
            curwirelength++; //현재 wire길이도 늘려주기
        }
        if (possible) {
            //지금까지의 거리 연결
            for (int j = 1; j <= curwirelength; j++) {
                int targetY = v[idx].y + dy[i] * j;
                int targetX = v[idx].x + dx[i] * j;
                //전선은 2로표시
                copymap[targetY][targetX] = 2;
            }
            //새로운거 보냄
            dfs(idx + 1, tempcorecnt, tempwirelength);
            //원복해주기
            for (int j = 1; j <= curwirelength; j++) {
                int targetY = v[idx].y + dy[i] * j;
                int targetX = v[idx].x + dx[i] * j;
                copymap[targetY][targetX] = map[targetY][targetX];
            }
        }
        else {
            //인덱스만 올리고 원래 있던 거 보내기
            dfs(idx + 1, corecnt, wirelength);
        }
    }

}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        setVector();
        memcpy(copymap, map, sizeof(map));
        dfs(0, 0, 0);
        cout << "#" << tc + 1 << " " << minWirelength << '\n';
    }
}