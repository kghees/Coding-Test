#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string s;
int main() {
    getline(cin, s);
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ' || s[i] < 65) continue;
        if (s[i] < 91 && s[i] > 64) {
            if (s[i] + 13 > 90)
                s[i] = s[i] + 13 - 26;
            else
                s[i] = s[i] + 13;
        }
        else if (s[i] > 96 && s[i] < 123) {
            if (s[i] + 13 > 122) {
                s[i] = s[i] + 13 - 26;
            }
            else
                s[i] = s[i] + 13;
        }
    }
    cout << s;
    return 0;
}
