#include <iostream>
#include <algorithm>
using namespace std;

int n;
int dat[26];
string res;
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        dat[s[0] - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        if (dat[i] >= 5) {
            res += (i + 'a');
        }
    }
    if (res.size())
        cout << res << '\n';
    else
        cout << "PREDAJA" << '\n';
    return 0;
}
