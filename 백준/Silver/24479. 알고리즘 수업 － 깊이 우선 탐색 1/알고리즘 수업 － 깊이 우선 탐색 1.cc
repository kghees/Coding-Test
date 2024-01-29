#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m, r, cnt=1;
vector<vector<int>> a;
vector<int>check;

void dfs(int x) {
	check[x] = cnt;
	for (auto i : a[x]) {
		if (!check[i]) {
			cnt++;
			dfs(i);
		}
	}
}
int main() {
	cin >> n >> m >> r;
	a.resize(n + 1);
	check.resize(n + 1);
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		a[u].push_back(v);
		a[v].push_back(u);
	}
	for (int i = 1; i <= n; i++) {
		sort(a[i].begin(), a[i].end());
	}
	dfs(r);
	for (int i = 1; i <= n; i++) {
		cout << check[i] << '\n';
	}
    return 0;
}
