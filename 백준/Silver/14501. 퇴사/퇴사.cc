#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
struct com {
	int day;
	int cost;
};
int n;
vector<com> v;
int res;

void dfs(int x, int cnt) {
	if (x > n) return;
	if (x == n) {
		res = max(res, cnt);
		return;
	}
	dfs(x + 1, cnt);
	dfs(x + v[x].day, cnt + v[x].cost);
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		v.push_back({ a,b });
	}
	dfs(0,0);
	cout << res;
	return 0;
}