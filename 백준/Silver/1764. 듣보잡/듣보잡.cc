#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n, m;
map<string, int> v;
vector<string> res;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        v[s] = 1;
    }
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        if (v[s] == 1) res.push_back(s);
    }
    sort(res.begin(), res.end());
    cout << res.size() << '\n';
    for (auto i : res) cout << i << '\n';
    return 0;
}