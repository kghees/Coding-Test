#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n;
int map[21][21];
int baby_shark = 2;
int dy[4] = { -1,0,1,0 };
int dx[4] = { 0,-1,0,1 };
int res;
int cnt;
int by, bx;
bool possible = false;

void bfs() {
	queue<pair<pair<int, int>, int>> q;
	q.push({ {by,bx},0 });
	bool visited[21][21] = { false };
	visited[by][bx] = true;
	int temp = 0;

	while (!q.empty()) {
		int y = q.front().first.first;
		int x = q.front().first.second;
		int sec = q.front().second;

		if (map[y][x] > 0 && map[y][x] < baby_shark && temp == sec) {
			if (by > y || (by == y && bx > x)) {
				by = y;
				bx = x;
				continue;
			}
		}
		q.pop();

		for (int k = 0; k < 4; k++) {
			int ny = y + dy[k];
			int nx = x + dx[k];

			if (ny < n && ny >= 0 && nx < n && nx >= 0 && !visited[ny][nx]) {
				if (map[ny][nx] <= baby_shark) {
					if (map[ny][nx] > 0 && map[ny][nx] < baby_shark && !possible) {
						possible = true;
						by = ny;
						bx = nx;
						temp = sec + 1;
						res += temp;
					}
					else {
						q.push({ {ny,nx},sec + 1 });
						visited[ny][nx] = true;
					}
				}
			}
		}
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 9) {
				by = i;
				bx = j;
				map[i][j] = 0;
			}
		}
	}
	while (true) {
		bfs();
		if (possible) {
			possible = false;
			cnt++;
			map[by][bx] = 0;

			if (cnt == baby_shark) {
				baby_shark += 1;
				cnt = 0;
			}
		}
		else break;
	}
	cout << res;
	return 0;
}
