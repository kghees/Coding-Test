#include<iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, k;
int d[101][100001];
vector<pair<int, int>> bag;

int main() {
	cin >> n >> k;
	bag.push_back({ 0,0 });
	for (int i = 0; i < n; i++) {
		int w, v;
		cin >> w >> v;
		bag.push_back({ w,v });
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			int weight = bag[i].first;
			int value = bag[i].second;

			if (j < weight) {
				d[i][j] = d[i - 1][j];
			}
			else {
				d[i][j] = max(d[i - 1][j - weight] + value, d[i - 1][j]);
			}
		}
	}
	cout << d[n][k];
	return 0;
}