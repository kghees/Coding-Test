#include<iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int n;

void dfs(int x, int st, int mid, int en) {
	if (x == 1) {
		cout << st << " " << en << '\n';
	}
	else {
		dfs(x - 1, st, en, mid);
		cout << st << " " << en << '\n';
		dfs(x - 1, mid, st, en);
	}
}

int main() {
	cin >> n;
	cout << (int)pow(2, n) - 1 << '\n';
	dfs(n, 1, 2, 3);
	return 0;
}