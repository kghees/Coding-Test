#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int n;

map<string, int> v;
vector<string> res;

bool cmp(string a, string b) {
    return a > b;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string a, b;
        cin >> a >> b;
        if (b == "enter") v[a] = 1;
        else v[a] = 0;
    }
    for (auto i : v) {
        if (i.second) res.push_back(i.first);
    }
    sort(res.begin(), res.end(),cmp);
    for (auto i : res) cout << i << '\n';
    return 0;
}