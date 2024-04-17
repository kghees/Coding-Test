#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
//Inorder순서로 들어옴
// 1 6 4 3 5 2 7 -> /2하면 3이 루트
//1 6 4 범위 5 2 7 범위에서 각각 /2하면 6 2
// 1 4 범위 5 7 범위 각각 /2 하면 1 4 5 7 순으로 들어와짐

int k;
int tree[1025];
vector<int> res[14];

void go(int x, int e, int lev) {
    if (x > e) return; // /2하는 문제이므로 x<=e가 충족되어야 하므로 써줘야함
    //0~0, 1~1구간까지 오면 기저사례
    if (x == e) {
        //push하고 종료만 시키면됨
        res[lev].push_back(tree[x]);
        return;
    }
    int mid = (x + e) / 2; //중간나눠서
    res[lev].push_back(tree[mid]); //중간값 푸쉬
    go(x, mid - 1, lev + 1); // 왼쪽 범위 탐색
    go(mid + 1, e, lev + 1); // 오른쪽 범위 탐색
    return;
}

int main() {
    cin >> k;
    int en = pow(2, k) - 1; //트리구조이므로 갯수는 2^k - 1개
    for (int i = 0; i < en; i++) {
        cin >> tree[i];
    }
    go(0, en, 1); //시작구간, 마지막구간, 깊이
    for (int i = 1; i <= k; i++) {
        for (int j : res[i]) {
            cout << j << " ";
        }
        cout << '\n';
    }
    return 0;
}