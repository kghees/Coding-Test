#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

string a[20001];
int n;

bool cmp(string x, string y) {
    if (x.length() == y.length()) return x < y;
    else return x.length() < y.length();
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n, cmp);
    for (int i = 0; i < n; i++) {
        if (a[i] == a[i - 1]) continue;
        cout << a[i] << '\n';
    }
    return 0;
}