#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
    while (true) {
        string s;
        getline(cin, s);
        vector<char> a;
        if (s == ".") break;
        int de = 1;
        for (int i = 0; i < s.length(); i++) {
            if (a.empty() && (s[i] == '(' || s[i] == ')' || s[i] == '[' || s[i] == ']')) {
                a.push_back(s[i]);
            }
            else if (s[i] == '(' || s[i] == '[') a.push_back(s[i]);
            else if (s[i] == ')') {
                if (a.back() == '(') a.pop_back();
                else a.push_back(s[i]);
            }
            else if (s[i] == ']') {
                if (a.back() == '[') a.pop_back();
                else a.push_back(s[i]);
            }
        }
        if (a.empty()) cout << "yes \n";
        else cout << "no \n";
    }
}
