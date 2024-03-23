#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int dp[64][64][64];
int arr[3];
int visited[64][64][64];
//공격 할 수 있는 총 경우의 수
int attack[6][3] = {
    {9,3,1},
    {9,1,3},
    {3,9,1},
    {3,1,9},
    {1,3,9},
    {1,9,3}
};
int n;
// 3개 이므로 구조체 만들어 쓰는게 편하다
struct A {
    int a, b, c;
};
queue<A>q;

int bfs(int a, int b, int c) {
    
    visited[a][b][c] = 1;
    q.push({ a,b,c });
    while (!q.empty()) {
        int a = q.front().a;
        int b = q.front().b;
        int c = q.front().c;
        q.pop();
        // 0 0 0 이 되면 끝
        if (visited[0][0][0]) break;
        //6개의 경우의 수에 대해
        for (int k = 0; k < 6; k++) {
            // 음수로 가는 것을 방지
            int na = max(0, a - attack[k][0]);
            int nb = max(0, b - attack[k][1]);
            int nc = max(0, c - attack[k][2]);
            // 이미 해봤으면 continue
            if (visited[na][nb][nc]) continue;
            //공격 횟수 추가
            visited[na][nb][nc] = visited[a][b][c] + 1;
            q.push({ na,nb,nc });
        }
    }
    //1부터 시작했으므로 1빼고 return
    return visited[0][0][0] - 1;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << bfs(arr[0], arr[1], arr[2]) << '\n';
    return 0;
}