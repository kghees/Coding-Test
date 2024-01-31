#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int n, m, st, cnt = 1;
vector<vector<int>> a;
vector<int>check;

void bfs(int x) {
	queue<int> q;
	q.push(x);
	check[x] = cnt;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		sort(a[x].begin(), a[x].end());
		for (int i : a[x]) {
			if (check[i] == 0) {
				cnt++;
				check[i] = cnt;
				q.push(i);
			}
		}
	}
}
int main() {
    cin >> n >> m >> st;
	a.resize(n + 1);
	check.resize(n + 1);
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		a[u].push_back(v);
		a[v].push_back(u);
	}
	bfs(st);
	for (int i = 1; i <= n; i++) {
		cout << check[i] << '\n';
	}
    return 0;
}