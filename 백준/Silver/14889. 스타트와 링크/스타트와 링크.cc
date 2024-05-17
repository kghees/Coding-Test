#include <iostream>
#include <algorithm>
using namespace std;

int n;
int map[21][21];
int st[11];
int li[11];
bool visited[11] = { false };
int res = 1e9;

void dfs(int idx, int lev) {
	// n/2명
	if (lev == n / 2) {
		//스타트 팀, 링크 팀 인덱스 넣기
		int cnt1 = 0, cnt2 = 0;
		for (int i = 0; i < n; i++) {
			//방문 한것들에 대해서는 스타트 팀
			if (visited[i]) {
				st[cnt1] = i;
				cnt1++;
			}
			//방문 안한것들에 대해서는 링크 팀
			else {
				li[cnt2] = i;
				cnt2++;
			}
		}
		int temp1 = 0, temp2 = 0;
		//각각 값 넣어주고
		for (int i = 0; i < n/2-1; i++) {
			for (int j = i+1; j < n/2; j++) {
				temp1 += map[st[i]][st[j]] + map[st[j]][st[i]];
				temp2 += map[li[i]][li[j]] + map[li[j]][li[i]];
			}
		}
		//최소 값 비교
		res = min(res, abs(temp1 - temp2));
		return;
	}
	else {
		//idx시작 : 중복 방지
		for (int i = idx; i < n; i++) {
			//방문 하지 않았으면
			if (!visited[i]) {
				//방문 체크하고
				visited[i] = true;
				dfs(i + 1, lev + 1); //다음 탐색
				visited[i] = false; //방문 해제
			}
		}
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}
	//중복 방지 인덱스, 팀원 수
	dfs(0, 0);
	cout << res;
	return 0;
}