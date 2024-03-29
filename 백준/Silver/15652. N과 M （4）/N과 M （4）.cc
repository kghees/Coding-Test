#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int arr[10];

void dfs(int x,int cnt) {
	if (cnt == m) {
		for (int i = 0; i < m; i++) {
			cout << arr[i] << " ";
		}
		cout << '\n';
		return;
	}
	for (int i = x; i <= n; i++) {
		arr[cnt] = i;
		dfs(i,cnt+1);
		arr[cnt] = 0;
	}
}

int main() {
	cin >> n >> m;
	dfs(1,0);

	return 0;
}
