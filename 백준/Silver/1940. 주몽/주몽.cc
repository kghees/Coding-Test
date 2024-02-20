#include <iostream>
using namespace std;
int n, m;
int arr[15001];
int res = 0;
int cnt = 0;
void dfs(int x,int y) {
    if (y == 2) {
        if (res == m)
            cnt++;
        return;
    }
    for (int i = x+1; i < n; i++) {
        res += arr[i];
        dfs(i,y+1);
        res -= arr[i];
    }
}
int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    dfs(-1,0);
    cout << cnt;
    return 0;
}