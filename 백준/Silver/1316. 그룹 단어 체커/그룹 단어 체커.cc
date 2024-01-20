#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;
    string s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        bool alphabet[26] = { false };
        alphabet[(int)s[0] - 97] = true;

        for (int i = 1; i < s.length(); i++) {
            if (s[i] == s[i - 1])
                continue;
            else if (s[i] != s[i - 1] && alphabet[(int)s[i] - 97] == true) {
                cnt++;
                break;
            }
            else {
                alphabet[(int)s[i] - 97] = true;
            }
        }
    }
    cout << n - cnt;
    return 0;
}