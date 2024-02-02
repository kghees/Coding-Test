#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int n, m, st;
vector<int> a[1001];
bool check[1001];
bool check1[1001];
void dfs(int x) {
    check[x] = true;
    cout << x << " ";
    for (int i : a[x]) {
        if (!check[i]) {
            check[i] = true;
            dfs(i);
        }
    }
}

void bfs(int x) {
    queue<int> q;
    q.push(x);
    check1[x] = true;
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        cout << x << " ";
        for (int i : a[x]) {
            if (!check1[i]) {
                check1[i] = true;
                q.push(i);
            }
        }
    }
}
int main() {
    cin >> n >> m >> st;
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        a[from].push_back(to);
        a[to].push_back(from);
    }
    for (int i = 1; i <= n; i++) {
        sort(a[i].begin(), a[i].end());
    }
    dfs(st);
    cout << '\n';
    bfs(st);
    return 0;
}