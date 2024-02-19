#include <iostream>
#include <algorithm>
using namespace std;
string s,res;
int cnt[200];
int flag;
char x;
int main() {
    cin >> s;
    for (char a : s) cnt[a]++;
    for (int i = 'Z'; i >= 'A'; i--) {
        if (cnt[i]) {
            if (cnt[i] & 1) {
                x = char(i);
                flag++;
                cnt[i]--;
            }
            if (flag == 2) break;
            for (int j = 0; j < cnt[i]; j += 2) {
                res = char(i) + res;
                res += char(i);
            }
        }
    }
    if (x)
        res.insert(res.begin() + res.size() / 2, x);
    if (flag == 2)
        cout << "I'm Sorry Hansoo\n";
    else
        cout << res << '\n';
    return 0;
}