#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int n, k;
int dat[200001];
int check[200001];
bool visited[200001] = { false };
vector<int> v;

void bfs(int x) {
    queue<int> q;
    q.push(x);
    dat[x] = 0;
    visited[x] = true;

    while (!q.empty()) {
        int x = q.front();
        q.pop();
        //k면 도착했으므로 return
        if (x == k) return;
        for (int nx : {x * 2, x + 1, x - 1}) {
            //범위안에 있고 방문하지 않았으면
            if (nx >= 0 && nx <= 200000 && !visited[nx]) {
                //시간 추가해주고
                dat[nx] = dat[x] + 1;
                //방문 체크 해주고
                visited[nx] = true;
                //check함수에 이전 값 넣어주기
                // ex) check[10] = 5, check[9] = 10, check[18] = 9, check[17] = 18 
                check[nx] = x;
                q.push(nx);
            }
        }
    }
}

int main() {
    cin >> n >> k;
    bfs(n);
    //동생위치부터 시작해서 수빈이 위치까지 check[i]로
    for (int i = k; i != n; i = check[i]) {
        v.push_back(i);
    }
    //수빈이 위치 안들어 갔으므로
    v.push_back(n);
    //거꾸로 뒤집어주기
    reverse(v.begin(), v.end());
    cout << dat[k] << '\n';
    for (int i : v) cout << i << " ";
    return 0;
}