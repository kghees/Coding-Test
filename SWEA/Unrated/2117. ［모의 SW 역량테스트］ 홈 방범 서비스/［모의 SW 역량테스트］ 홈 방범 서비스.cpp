#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int t, n, m;
int map[21][21];
int res;

void init() {
	memset(map, sizeof(map), 0);
	res = 0;
}

void input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}
}

void check() {
	for (int k = 1; k <= n + 1; k++) {
		int cost = k * k + (k - 1) * (k - 1);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int cnt = 0;
				bool visited[21][21] = { false };

				for (int a = 0; a < k; a++) {
					int ny1 = i + a;
					int ny2 = i - a;

					for (int b = -(k - a) + 1; b < k - a; b++) {
						int nx = j + b;

						if (ny1 < n && ny1 >= 0 && nx < n && nx >= 0) {
							if (map[ny1][nx] == 1 && !visited[ny1][nx]) {
								cnt++;
								visited[ny1][nx] = true;
							}
						}
						if (ny2 < n && ny2 >= 0 && nx < n && nx >= 0) {
							if (map[ny2][nx] == 1 && !visited[ny2][nx]) {
								cnt++;
								visited[ny2][nx] = true;
							}
						}
					}
				}
				int ans = (cnt*m - cost);
				if (ans >= 0 && res < cnt) res = cnt;
			}
		}
		
	}
}



int main() {
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		init();
		input();
		check();
		cout << "#" << tc + 1 << " " << res << '\n';
	}
	return 0;
}