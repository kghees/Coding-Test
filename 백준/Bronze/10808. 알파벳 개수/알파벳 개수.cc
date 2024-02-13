#include <iostream>
using namespace std;
int dat[26] = { 0 };
string s;
int main() {
    cin >> s;
    for (int i = 0; i < s.length(); i++) {
        dat[s[i] - 97] += 1;
    }
    for (int i = 0; i < 26; i++) {
        cout << dat[i] << " ";
    }
    return 0;
}