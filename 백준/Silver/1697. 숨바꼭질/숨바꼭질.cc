#include <iostream>
#include <queue>
using namespace std;
int s, d;
int tv[200001];
bool check[200001] = { false };
void bfs(int x) {
	queue<int> q;
	q.push(x);
	tv[x] = 0;
	check[x] = true;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int nx : {x * 2, x + 1, x - 1}) {
			if (nx >= 0 && nx <= 200000 && !check[nx]) {
				check[nx] = true;
				tv[nx] = tv[x] + 1;
				q.push(nx);
			}
		}
	}
}
int main() {
	cin >> s >> d;
	bfs(s);
	cout << tv[d];
	return 0;
}