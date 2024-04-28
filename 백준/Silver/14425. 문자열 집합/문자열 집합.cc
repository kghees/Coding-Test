#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
vector<string> v;


int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        v.push_back(s);
    }
    sort(v.begin(), v.end());

    int cnt = 0;
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        if (binary_search(v.begin(),v.end(), s)) cnt++;
    }
    cout << cnt;
    return 0;
}