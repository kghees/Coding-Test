#include <iostream>
#include <vector>
using namespace std;
int n, t, cnt;
vector<vector<int>> arr;
vector<bool> check;

void dfs(int x) {
	check[x] = true;
	for (auto i : arr[x]) {
		if (!check[i]) {
			check[i] = true;
			cnt += 1;
			dfs(i);
		}
	}
}
int main() {
	cin >> n >> t;
	arr.resize(n + 1);
	check.resize(n + 1, false);
	for (int i = 0; i < t; i++) {
		int u, v;
		cin >> u >> v;
		arr[u].push_back(v);
		arr[v].push_back(u);
	}
	dfs(1);
	cout << cnt;
    return 0;
}
