#include <iostream>
using namespace std;

int n;

int dfs(int x) {
    if (x == 0) return 0;
    if (x == 1) return 1;
    return dfs(x - 1) + dfs(x - 2);
}

int main() {
    cin >> n;
    cout << dfs(n);
    return 0;
}