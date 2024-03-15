#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int n, m;
vector<int> v[10001];
bool visited[10001];
int dat[10001];
int maxres = 0;

int dfs(int x) {
	//방문 체크 해주기
	visited[x] = true;
	//처음 들어오는 번호 세므로 cnt는 1부터 시작
	int cnt = 1;
	//v[x]에 들어 있는 번호들에 대해 탐색
	for (int i : v[x]) {
		//방문 한거는 pass
		if (visited[i]) continue;
		//방문 체크
		visited[i] = true;
		//번호가 있다면 cnt가 1을 들고 있으므로 1씩 더해진다.
		cnt += dfs(i);
	}
	return cnt;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		//역으로 탐색해야하므로 b에 a를 넣어주기 
		v[b].push_back(a);
	}
	for (int i = 1; i <= n; i++) {
		//다 돌려야 하므로 돌때 마다 visited 초기화 해주기
		memset(visited, 0, sizeof(visited));
		//i마다 해킹 할 수 있는 컴퓨터 수 받기
		int temp = dfs(i);
		//i번째 해당하는 dat배열에 컴퓨터 수 넣어주고
		dat[i] = temp;
		//max값 찾아주기
		maxres = max(temp, maxres);
	}
	//max값과 같은 컴퓨터 번호 다 출력 해주기
	for (int i = 1; i <= n; i++) {
		if (maxres == dat[i]) cout << i << " ";
	}
	return 0;
}