#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

int n, k;
int dat[200001];
bool visited[200001] = { false };

void bfs(int x) {
    deque<int> q;
    q.push_back(x);
    visited[x] = true;
    dat[x] = 0;

    while (!q.empty()) {
        int x = q.front();
        q.pop_front();
        
        if (!visited[2 * x] && 2 * x <= 200000) {
            visited[2 * x] = true;
            dat[2 * x] = dat[x];
            q.push_front(2 * x);
        }
        if (!visited[x - 1] && x - 1 >= 0) {
            visited[x - 1] = true;
            dat[x - 1] = dat[x] + 1;
            q.push_back(x - 1);
        }
        if (!visited[x + 1] && x + 1 <= 200000) {
            visited[x + 1] = true;
            dat[x + 1] = dat[x] + 1;
            q.push_back(x + 1);
        }
    }
}

int main() {
    cin >> n >> k;
    bfs(n);
    cout << dat[k];
    return 0;
}