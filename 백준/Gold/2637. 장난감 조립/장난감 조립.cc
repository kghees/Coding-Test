#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n, m;
vector<pair<int, int>> toy[101];
int dat[101];
int res[101];
vector<int> basic;

void make() {
    queue<int> q;
    q.push(n);
    res[n] = 1;

    while (!q.empty()) {
        int now = q.front();
        q.pop();
        if (toy[now].size() == 0) {
            basic.push_back(now);
        }
        for (auto i : toy[now]) {
            int x = i.first;
            int y = i.second;
            res[x] += res[now] * y;
            dat[x]--;
            if (!dat[x]) q.push(x);
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        toy[a].push_back({ b,c });
        dat[b]++;
    }
    make();
    sort(basic.begin(), basic.end());
    for (auto i : basic) cout << i << " " << res[i] << '\n';
    return 0;
}