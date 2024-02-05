#include <iostream>
using namespace std;
int n, m;
int arr[9];
bool check[9] = { false };
void dfs(int x) {
    if (x == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << " ";
        }
        cout << '\n';
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (check[i]) continue;
        arr[x] = i;
        check[i] = true;
        dfs(x + 1);
        check[i] = false;
        arr[x] = 0;
    }
}
int main() {
    cin >> n >> m;
    dfs(0);
    return 0;
}