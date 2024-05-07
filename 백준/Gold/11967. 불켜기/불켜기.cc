#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct coco {
	int y, x;
	int light;
};

int n, m;
int map[101][101];
int dy[4] = { 0,0,-1,1 };
int dx[4] = { -1,1,0,0 };
vector<coco> v[101][101];

bool bfs() {
	queue<coco> q;
	q.push({ 1,1,0 });
	bool visited[101][101] = { false };
	visited[1][1] = true;
	int flag = 0; //불 킬 수 있는지 없는지 체크할 변수
	while (!q.empty()) {
		coco now = q.front();
		q.pop();

		//불 킬 수 있는거 먼저 키기
		for (int i = 0; i < v[now.y][now.x].size(); i++) {
			if (v[now.y][now.x][i].light == 0) {
				flag = 1; //불 킬 수 있다고 체크
				v[now.y][now.x][i].light = 1; // 현재 좌표 상태 바꿔주고
				map[v[now.y][now.x][i].y][v[now.y][now.x][i].x] = 1;//맵에 불 켜주기
			}
		}
		//다음 방 이동 하기
		for (int k = 0; k < 4; k++) {
			int ny = now.y + dy[k];
			int nx = now.x + dx[k];

			if (ny > n || ny <= 0 || nx > n || nx <= 0) continue;
			if (!map[ny][nx] || visited[ny][nx]) continue;
			visited[ny][nx] = true;
			q.push({ ny,nx });
		}
	}
	if (flag)return true;
	else return false;
} 

int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		v[a][b].push_back({ c,d,0 });
	}
	//시작점 불키기
	map[1][1] = 1;
	while(bfs()){}

	int res = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (map[i][j]) res++;
		}
	}
	cout << res;
	return 0;
}