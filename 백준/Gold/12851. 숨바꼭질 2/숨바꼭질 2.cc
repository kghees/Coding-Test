#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int n, k;
int dat[200001];
bool visited[200001] = { false };
int cnt[200001];

void bfs(int x) {
    queue<int> q;
    q.push(x);
    visited[x] = true;
    dat[x] = 0;
    cnt[x] = 1;
    while (!q.empty()) {
        int x = q.front();
        q.pop();

        for (int nx : {x - 1, x + 1, x * 2}) {
            if (nx >= 0 && nx <= 100000) {
                if (!visited[nx]) {
                    q.push(nx);
                    visited[nx] = true;
                    dat[nx] = dat[x] + 1;
                    cnt[nx] += cnt[x];
                }
                else if (dat[nx] == dat[x] + 1) {
                    cnt[nx] += cnt[x];
                }
            }
        }
    }
}

int main() {
    cin >> n >> k;
    bfs(n);
    cout << dat[k] << '\n' << cnt[k];
    return 0;
}