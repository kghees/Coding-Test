#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n, m, st;
vector<int> arr[200001];
int check[200001] = { 0 };
int cnt = 1;
void dfs(int x) {
    check[x] = cnt;
    for (int i : arr[x]) {
        if (!check[i]) {
            cnt++;
            dfs(i);
        }
    }
}
int main() {
    cin >> n >> m >> st;
    int u, v;
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        arr[u].push_back(v);
        arr[v].push_back(u);
    }
    for (int i = 1; i <= n; i++) {
        sort(arr[i].begin(), arr[i].end(), greater<int>());
    }
    dfs(st);
    for (int i = 1; i <= n; i++)
        cout << check[i] << '\n';
    return 0;
}
