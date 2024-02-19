#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
int t,n;
int main() {
    cin >> t;
    while (t--) {
        map<string, int> m;
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            string a, b;
            cin >> a >> b;
            m[b]++;
        }
        int res = 1;
        for (auto c : m) {
            res *= ((int)c.second + 1);
        }
        res--;
        cout << res << '\n';

    }
    return 0;
}