#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int n;
int root;
int r;
vector<int> tree[51];

//리프 노드 수를 구하는 함수
int dfs(int x) {
    int res = 0;
    int child = 0;
    for (int i : tree[x]) {
        //지우는 것은 continue 세지 않아야 하므로 (탐색X)
        if (i == r) continue;
        //재귀 돌면서 child없으면 return 1이므로 리프 노드 수 더해주고 있음
        res += dfs(i);
        //자식 노드가 있으면 child수 더해주기
        child++;
    }
    //child가 없으면 리프노드 이므로 1
    if (!child) return 1;
    return res;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        //root 따로 체킹
        if (a == -1) root = i;
        //ex) (0:1,2), (1:3,4)
        else tree[a].push_back(i);
    }
    cin >> r;
    //r이 root와 같으면 다 지워지므로 0
    if (r == root) {
        cout << 0;
        return 0;
    }
    else cout << dfs(root);

    return 0;
}
