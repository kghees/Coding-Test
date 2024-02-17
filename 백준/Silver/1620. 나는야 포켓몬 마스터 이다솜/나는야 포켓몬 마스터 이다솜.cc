#include <iostream>
#include <map>
using namespace std;
int n, m;
map<string, int> mp;
map<int, string> mp1;
string a[100001];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        mp[s] = i;
        mp1[i] = s;
        a[i] = s;
    }
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        if (atoi(s.c_str()) == 0) { //0이면 문자열
            cout << mp[s] << '\n';
        }
        else { // 아니라면 숫자
            cout << a[atoi(s.c_str())] << '\n';
        }

    }
    return 0;
}
