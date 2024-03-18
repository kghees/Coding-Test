#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
int map[51][51];
int res = 1e9;
vector<vector<int>> chickenList;
vector<pair<int, int>> home;
vector<pair<int, int>> chicken;

void combi(int start, vector<int> v) {
	//m개 만큼 치킨집 골랐으면
	if (v.size() == m) {
		//고른 목록 chickenList에 push해주기
		chickenList.push_back(v);
		return;
	}
	//중복 피해야 하므로 start+1부터
	for (int i = start + 1; i < chicken.size(); i++) {
		//넣어주고
		v.push_back(i);
		//다음으로
		combi(i, v);
		//다른 경우도 생각해야하니 빼주기
		v.pop_back();
	}
	return;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) home.push_back({ i,j });
			if (map[i][j] == 2) chicken.push_back({ i,j });
		}
	}
	vector<int> v;
	//치킨집 조합 짜기
	combi(-1, v);
	// 조합짠거를 기반으로 
	for (vector<int> cList : chickenList) {
		//도시의 치킨 거리 넣을 변수
		int ret = 0;
		//집의 좌표와 좌표수 만큼
		for (pair<int, int> h : home) {
			// 치킨 거리 넣을 변수
			int temp = 1e9;
			// 치킨집 조합 짠거로
			for (int i : cList) {
				// 치킨 거리 구해주고
				int dist = abs(h.first - chicken[i].first) + abs(h.second - chicken[i].second);
				//해당 집에 대한 치킨거리 최소값을
				temp = min(dist, temp);
			}
			//ret에 더해주고
			ret += temp;
		}
		//최종 도시의 치킨거리의 최소 값 찾아주기
		res = min(ret, res);
	}
	cout << res << '\n';
	return 0;
}