#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        vector<char> a;
        for (int j = 0; j < s.length(); j++) {
            if (a.empty())
                a.push_back(s[j]);
            else if (s[j] == ')') {
                if (a.back() == '(') a.pop_back();
                else a.push_back(s[j]);
            }
            else a.push_back(s[j]);
        }
        if (a.empty()) cout << "YES \n";
        else cout << "NO \n";
    }
    return 0;
}
