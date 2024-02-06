#include <iostream>
using namespace std;
int r, c, t, ds = 0;
int x1,x2;
int dust[51][51];
int arr[51][51];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };

void spread() {
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (dust[i][j] == -1 || dust[i][j] == 0) continue;
			int cnt = 0;
			int temp = dust[i][j]/5;

			for (int k = 0; k < 4; k++) {
				int nx = i + dx[k];
				int ny = j + dy[k];
				if (nx >= r || nx < 0 || ny >= c || ny < 0) continue;
				if (dust[nx][ny] == -1) continue;

				cnt++;
				arr[nx][ny] += temp;
			}
			dust[i][j] = dust[i][j] - (temp * cnt);
		}
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (dust[i][j] != -1) {
				dust[i][j] += arr[i][j];
				arr[i][j] = 0;
			}
		}
	}
}

void air() {
	//위쪽 방향
	
	//왼쪽
	for (int i = x1 - 1; i >= 0; i--) {
		dust[i + 1][0] = dust[i][0];
	}
	//위쪽
	for (int i = 0; i < c - 1; i++) {
		dust[0][i] = dust[0][i + 1];
	}
	//오른쪽
	for (int i = 0; i < x1; i++) {
		dust[i][c - 1] = dust[i + 1][c - 1];
	}
	//아래쪽
	for (int i = c - 1; i > 1; i--) {
		dust[x1][i] = dust[x1][i - 1];
	}
	
	dust[x1][1] = 0;
	dust[x1][0] = -1;

	//아래쪽 방향
	//왼쪽
	for (int i = x2; i < r; i++) {
		dust[i][0] = dust[i + 1][0];
	}
	//아래쪽
	for (int i = 0; i < c - 1; i++) {
		dust[r - 1][i] = dust[r - 1][i + 1];
	}
	//오른쪽
	for (int i = r - 1; i > x2; i--) {
		dust[i][c - 1] = dust[i - 1][c - 1];
	}
	// 위쪽
	for (int i = c - 1; i > 1; i--) {
		dust[x2][i] = dust[x2][i - 1];
	}
	dust[x2][0] = -1;
	dust[x2][1] = 0;

}
int main() {
	cin >> r >> c >> t;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> dust[i][j];
			if (dust[i][j] == -1) {
				if (x1 == 0) x1 = i;
				else x2 = i;
			}
		}
	}
	for (int i = 0; i < t; i++) {
		spread();
		air();
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (dust[i][j] > 0) {
				ds += dust[i][j];
			}
		}
	}
	cout << ds;
	return 0;
}