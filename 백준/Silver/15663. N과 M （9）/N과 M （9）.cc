#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int arr[9];
int res[9];
bool check[10] = { false };

void dfs(int lev) {
	if (lev == m) {
		for (int i = 0; i < m; i++) {
			cout << res[i] << " ";
		}
		cout << '\n';
		return;
	}
	int temp = 0;
	for (int i = 0; i < n; i++) {
		if (!check[i] && temp != arr[i]) {
			res[lev] = arr[i];
			temp = res[lev];
			check[i] = true;
			dfs(lev + 1);
			check[i] = false;
		}
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	dfs(0);
	return 0;
}           