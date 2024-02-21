#include <iostream>
#include <stack>
using namespace std;
int n;
int cnt = 0;
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        stack<char> stk;
        for (char a : s) {
            if (stk.size() && stk.top() == a) stk.pop();
            else stk.push(a);
        }
        if (stk.empty()) cnt++;
    }
    cout << cnt;
    return 0;
}