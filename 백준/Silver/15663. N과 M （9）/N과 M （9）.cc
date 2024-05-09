#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int arr[9];
int res[9];
bool check[10] = { false };

void dfs(int lev) {
	//출력해야 될 수와 같아지면 출력
	if (lev == m) {
		for (int i = 0; i < m; i++) {
			cout << res[i] << " ";
		}
		cout << '\n';
		return;
	}
	//그 전 수와 for문에서 같은지 비교해주기 위해 변수 하나 만듬
	int temp = 0;
	for (int i = 0; i < n; i++) {
		//체크되지 않았고 재귀 돌아왔을 때 이전수와 현재수가 같지 않으면
		if (!check[i] && temp != arr[i]) {
			res[lev] = arr[i]; //결과 값 배열에 넣고
			temp = res[lev]; //temp 새로운 수로 넣어주고
			check[i] = true; // 방문 체크해주고
			dfs(lev + 1); 
			check[i] = false; //다음 탐색을 위해 방문 해제
			res[lev] = 0;
		}
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	//같은 숫자 전 인덱스와 배열하기 위해 sort
	sort(arr, arr + n);
	dfs(0);
	return 0;
}      