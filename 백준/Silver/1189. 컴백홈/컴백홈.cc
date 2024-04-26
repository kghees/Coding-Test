#include <iostream>
#include <algorithm>
using namespace std;

int r, c, k;
char map[6][6];
int res;
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
bool visited[6][6] = { false };

void dfs(int y, int x) {
	visited[y][x] = true;
	if (y == 0 && x == c - 1) {
		int cnt = 0;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (visited[i][j]) cnt++;
			}
		}
		if (cnt == k) res++;
		return;
	}
	for (int k = 0; k < 4; k++) {
		int ny = y + dy[k];
		int nx = x + dx[k];

		if (ny < r && ny >= 0 && nx < c && nx >= 0) {
			if (!visited[ny][nx] && map[ny][nx] != 'T') {
				visited[ny][nx] = true;
				dfs(ny, nx);
				visited[ny][nx] = false;
			}
		}
	}
}

int main() {
	cin >> r >> c >> k;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> map[i][j];
		}
	}
	dfs(r - 1, 0);
	cout << res;
	return 0;
}