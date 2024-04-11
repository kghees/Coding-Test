#include<iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t, d, w, k;
int map[14][21];
int copy_map[14][21];
int res;

void init() {
	memset(map, 0, sizeof(map));
	memset(copy_map, 0, sizeof(copy_map));
	res  = 1e9;
}

void input() {
	cin >> d >> w >> k;
	for (int i = 0; i < d; i++) {
		for (int j = 0; j < w; j++) {
			cin >> map[i][j];
			copy_map[i][j] = map[i][j];
		}
	}
}

bool check() {
	int check_cnt = 0;
	for (int i = 0; i < w; i++) {
		int a_cnt = 0, b_cnt = 0;

		for (int j = 0; j < d; j++) {
			if (copy_map[j][i] == 0) {
				a_cnt++;
				b_cnt = 0;
			}
			else if (copy_map[j][i] == 1) {
				a_cnt = 0;
				b_cnt++;
			}
			if (a_cnt >= k || b_cnt >= k) {
				check_cnt++;
				break;
			}
		}
		if (a_cnt < k && b_cnt < k) return false;
	}
	if (check_cnt == w) return true;
	else return false;
}

void insert_drug(int temp, int idx) {
	for (int i = 0; i < w; i++) {
		copy_map[idx][i] = temp;
	}
}

void turn_drug(int idx) {
	for (int i = 0; i < w; i++) {
		copy_map[idx][i] = map[idx][i];
	}
}

void dfs(int x, int cnt) {
	if (res < cnt) return; //이미 결과 값이 더 작은 경우 return
	if (x == d) {
		if (check()) {
			res = min(res, cnt);
		}
		return;
	}
	dfs(x + 1, cnt); //투입 안할 때
	insert_drug(0, x);
	dfs(x + 1, cnt + 1); //A 약품 투입
	insert_drug(1, x);
	dfs(x + 1, cnt + 1);
	turn_drug(x);
}

int main() {
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		init();
		input();
		if (check()) {
			cout << "#" << tc + 1 << " " << 0 << '\n';
		}
		else {
			dfs(0, 0);
			cout << "#" << tc + 1 << " " << res << '\n';
		}
	}
	return 0;
}