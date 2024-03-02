#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
int n, c;
int a[1004];
map<int, int> mp;
map<int, int> mp_first;
vector<pair<int, int>> v;

bool cmp(pair<int, int>a, pair<int, int> b) {
    if (a.first == b.first) { //같으면
        return mp_first[a.second] < mp_first[b.second]; //먼저 나온 거
    }
    return a.first > b.first; // 빈도 수 먼저
}

int main() {
    cin >> n >> c;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mp[a[i]]++;
        //map은 할당되지 않아있으면 0이므로 이 점을 활용
        //i가 0부터이므로 i+1유의 하기
        if (mp_first[a[i]] == 0) mp_first[a[i]] = i + 1;
    }
    for (auto i : mp) {
        v.push_back({ i.second,i.first });
    }
    sort(v.begin(), v.end(), cmp);
    for (auto i : v) {
        for (int j = 0; j < i.first; j++) {
            cout << i.second << " ";
        }
    }
    return 0;
}