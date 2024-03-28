#include <iostream>
#include <algorithm>
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
        arr[x] = i;
        dfs(x + 1);
        arr[x] = 0;
    }
}

int main() {
    cin >> n >> m;
    dfs(0);
    return 0;
}