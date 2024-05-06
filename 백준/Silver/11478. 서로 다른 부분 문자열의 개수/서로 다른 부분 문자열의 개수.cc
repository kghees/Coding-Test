#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

string s;
set<string> res;
int main() {
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        string v = "";
        for (int j = i; j < s.size(); j++) {
            v += s[j];
            res.insert(v);
        }
        v = "";
    }
    cout << res.size();
    return 0;
}