#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t, n, l;
int map[21][21];
int res;

void init() {
    memset(map, 0, sizeof(map));
    res = 0;
}

void input() {
    cin >> n >> l;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
}

void row(int y, int x, int cnt) {
    int cur = map[y][x]; //현재 값
    int next = map[y][x + 1]; //다음 값
    //n-1까지 왔으면 활주로 건설 할 수 있는 것임
    if (x == n - 1) {
        res++;
        return;
    }

    //현재 값과 다음 값이 같을 때
    //다음으로 가면 됨
    if (cur == next) row(y, x + 1, cnt + 1);

    //현재 값보다 다음 값이 1 클 때
    else if (cur + 1 == next) {
        if (cnt >= l) { //l개만큼 경사로를 놓을 수 있다면
            row(y, x + 1, 1); //놓고 놓을 수 있는 경사로는 1로 초기화
        }
    }

    //현재 값이 다음 값보다 1 클 때
    else if (cur == next + 1) {
        if (x + l < n) { //l개를 놔도 범위를 벗어 나지 않고
            //l개까지 모두 next 값과 같은지 확인
            for (int i = x + 1; i < x + 1 + l; i++) {
                if (map[y][i] != next) return;
            }
            row(y, x + l, 0); //같다면 l개를 놓고 놓을 수 있는 경사로는 0개로 초기화
        }
    }
}

void col(int y, int x, int cnt) {
    int cur = map[y][x];
    int next = map[y + 1][x]; 
    
    if (y == n - 1) {
        res++;
        return;
    }

    
    if (cur == next) col(y + 1, x, cnt + 1);

    
    else if (cur + 1 == next) {
        if (cnt >= l) { 
            col(y + 1, x, 1); 
        }
    }

    
    else if (cur == next + 1) {
        if (y + l < n) { 
            
            for (int i = y + 1; i < y + 1 + l; i++) {
                if (map[i][x] != next) return;
            }
            col(y + l, x, 0); 
        }
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();

        for (int i = 0; i < n; i++) {
            row(i, 0, 1); //행은 y좌표 고정
            col(0, i, 1); //열은 x좌표 고정
        }
        cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}
