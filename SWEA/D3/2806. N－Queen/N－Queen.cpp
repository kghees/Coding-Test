#include <iostream>
#include <algorithm>
using namespace std;
int t,n,cnt = 0;
int d[11];
bool check(int x) {
    for (int i = 0; i < x; i++) {
        if (d[x] == d[i] || abs(d[x] - d[i]) == x - i)
            return false;
    }
    return true;
}
void dfs(int x) {
    if (x == n) {
        cnt++;
        return;
    }
    else {
        for (int i = 0; i < n; i++) {
            d[x] = i;
            if (check(x))
                dfs(x + 1);
        }
    }

}
int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        cnt = 0;
        dfs(0);
        cout << "#" << i + 1 << " " << cnt << '\n';
    }
    return 0;
}