#include<iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int r, c;
char map[21][21];
int res;
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
int dat[27] = { 0 };

void dfs(int y, int x, int cnt) {
	res = max(res, cnt);
	for (int k = 0; k < 4; k++) {
		int ny = y + dy[k];
		int nx = x + dx[k];

		if (ny < r && ny >= 0 && nx < c && nx >= 0) {
			if (!dat[map[ny][nx] - 65]) {
				dat[map[ny][nx] - 65] = 1;
				dfs(ny, nx, cnt + 1);
				dat[map[ny][nx] - 65] = 0;
			}
		}
	}
	
}

int main() {
	cin >> r >> c;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> map[i][j];
		}
	}

	dat[map[0][0] - 65] = 1;
	dfs(0, 0, 1);

	cout << res;
	return 0;
}