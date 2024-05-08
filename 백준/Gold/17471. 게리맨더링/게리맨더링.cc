#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int n,human_sum;
int human[11];
int dat[11];
int res = 1e9;
bool visited[11] = { false };
vector<int> v[11];

void bfs(int x) {
	queue<int> q;
	q.push(x);
	visited[x] = true;

	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int i : v[now]) {
			if (!visited[i] && dat[i] == dat[x]) {
				q.push(i);
				visited[i] = true;
			}
		}
	}
}


bool check() {
	//다른 조합들 위해 항상 초기화
	memset(visited, false, sizeof(visited));
	int cnt = 0;

	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			bfs(i);
			cnt++;
		}
	}
	//2개 지역구니깐 연결되어있다면 2번 돌고 나와야함??
	if (cnt == 2) return true;
	else return false;
}


void dfs(int x) {
	if (x == n) {
		if (check()) {
			int temp1 = 0;
			for (int i = 1; i <= n; i++) {
				if (dat[i]) temp1 += human[i];
			}
			int temp2 = human_sum - temp1;
			int ans = abs(temp2 - temp1);
			res = min(res, ans);
		}
		return;
	}
	dat[x] = 1;
	dfs(x + 1);
	dat[x] = 0;
	dfs(x + 1);
}

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> human[i];
		human_sum += human[i];
	}
	
	for (int i = 1; i <= n; i++) {
		int a;
		cin >> a;
		for (int j = 0; j < a; j++) {
			int b;
			cin >> b;
			v[i].push_back(b);
		}
	}
	dfs(1);
	if (res == 1e9) cout << -1;
	else cout << res;
	return 0;
}
