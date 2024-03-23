#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n;
string s;
vector<int> num;
vector<char> oper_str;
int res = -987654321;
int oper(char a, int b, int c) {
    if (a == '+') return b + c;
    if (a == '-') return b - c;
    if (a == '*') return b * c;
}

void go(int cnt, int x) {
    if (cnt == num.size() - 1) {
        res = max(res, x);
        return;
    }
    go(cnt + 1, oper(oper_str[cnt], x, num[cnt + 1]));
    if (cnt + 2 <= num.size() - 1) {
        int temp = oper(oper_str[cnt + 1], num[cnt + 1], num[cnt + 2]);
        go(cnt + 2, oper(oper_str[cnt], x, temp));
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) num.push_back(s[i] - '0');
        else oper_str.push_back(s[i]);
    }
    go(0, num[0]);
    cout << res << '\n';
    return 0;
}