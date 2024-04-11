#include<iostream>
#include <algorithm>
#include <queue>
using namespace std;

int n;
int map[21][21];
int baby_shark = 2;
int dy[4] = { -1,0,1,0 }; //상좌하우
int dx[4] = { 0,-1,0,1 };
int res; //최종 시간
int cnt; //물고기 먹은 횟수
int by, bx; //아기 상어 위치
bool possible = false; //물고기 먹었는지 판단

void bfs() {
	queue<pair<pair<int, int>, int>> q;
	q.push({{by,bx},0}); //아기상어 시작위치 및 걸린 시간
	bool visited[21][21] = { false };
	visited[by][bx] = true;
	int temp = 0; //현재까지 걸린 시간

	while (!q.empty()) {
		int y = q.front().first.first;
		int x = q.front().first.second;
		int sec = q.front().second;
		//상 -> 좌 순으로 먹게해야함 
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
			//범위안에 있고 방문하지 않았는데
			if (ny < n && ny >= 0 && nx < n && nx >= 0 && !visited[ny][nx]) {
				//아기 상어 크기보다 작거나 같은데
				if (map[ny][nx] <= baby_shark) {
					// 아기상어가 더 크고 아직 물고기를 먹지 않았다면
					if (map[ny][nx] > 0 && map[ny][nx] < baby_shark && !possible) {
						possible = true; //먹음 처리
						by = ny, bx = nx; //먹은 자리가 아기상어 위치
						temp = sec + 1; //먹으러 이동한 시간+1
						res += temp; //최종시간에 더해주기
					}
					//못먹었을때
					else {
						q.push({ {ny,nx},sec + 1 }); //이동시간만 +1해서 q에
						visited[ny][nx] = true; //방문 체크
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
			if (map[i][j] == 9) by = i, bx = j, map[i][j] = 0;
		}
	}
	while (true) {
		bfs();
		//물고기를 먹었을 때
		if (possible) {
			possible = false; //다음 먹었는지 판당을 위해 false
			cnt++; //물고기 먹은 것이므로 +1
			//물고기 먹은 자리 0으로 만들어주기
			map[by][bx] = 0; //먹었다면 마지막 아기상어 위치가 먹은 자리임
			//먹은 물고기 수와 아기상어 크기가 일치하다면
			if (cnt == baby_shark) {
				baby_shark += 1;
				cnt = 0;
			}
		}
		//물고기 먹을 게 없으면 엄마 call
		else {
			break;
		}
	}
	cout << res;
	return 0;
}