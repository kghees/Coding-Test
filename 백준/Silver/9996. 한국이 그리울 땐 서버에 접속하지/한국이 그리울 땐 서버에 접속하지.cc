#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int n;
string s;
int main() {
    cin >> n >> s;
    string pre, suf;
    int pos = s.find('*');
    pre = s.substr(0, pos);
    suf = s.substr(pos + 1);
    for (int i = 0; i < n; i++) {
        string a;
        cin >> a;
        if (pre.size() + suf.size() > a.size())
            cout << "NE" << '\n';
        else {
            if (pre == a.substr(0, pre.size()) && suf == a.substr(a.size() - suf.size()))
                cout << "DA" << '\n';
            else
                cout << "NE" << '\n';
        }
    }
    return 0;
}
