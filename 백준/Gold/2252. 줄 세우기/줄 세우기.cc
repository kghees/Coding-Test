#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n, m;
int dat[32001];
vector<int> student[32001];

void line_up() {
	queue<int> q;
	//
	for (int i = 1; i <= n; i++) {
		if (!dat[i]) q.push(i);
	}
	for (int i = 0; i < n; i++) {
		int now = q.front();
		q.pop();
		cout << now << " ";
		for (int x : student[now]) {
			dat[x]--;
			if (!dat[x]) q.push(x);
		}
	}
	
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		student[a].push_back(b);
		dat[b]++;
	}
	line_up();
	return 0;
}