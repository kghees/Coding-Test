#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
vector<int> a[100001];
vector<int> res;
int temp[100001];
int order[100001];
bool visited[100001] = { false };

bool cmp(int x, int y) {
	return order[x] < order[y];
}

void dfs(int x) {
	if (visited[x]) return;

	visited[x] = true;
	res.push_back(x);
	for (int i : a[x]) {
		if (!visited[i]) dfs(i);
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int u, v;
		cin >> u >> v;
		a[u].push_back(v);
		a[v].push_back(u);
	}

	for (int i = 1; i <= n; i++) {
		cin >> temp[i];
		order[temp[i]] = i;
	}
	for (int i = 1; i <= n; i++) {
		sort(a[i].begin(), a[i].end(), cmp);
	}
	res.push_back(0);
	dfs(1);
	int flag = 1;
	for (int i = 1; i <= n; i++) {
		if (temp[i] != res[i]) {
			flag = 0;
			break;
		}
	}
	if (flag) cout << 1;
	else cout << 0;
	return 0;
}