#include <iostream>
#include <algorithm>
using namespace std;
int n;
int num[12];
int arr[4];
int maxi = -21e8;
int mini = 21e8;

void dfs(int x, int temp, int plus, int sub, int mul, int div) {
    if (x == n) {
        maxi = max(maxi, temp);
        mini = min(mini, temp);
        return;
    }
    if (plus)
        dfs(x + 1, temp + num[x],plus-1, sub, mul, div);
    if (sub)
        dfs(x + 1, temp - num[x], plus, sub - 1, mul, div);
    if (mul)
        dfs(x + 1, temp * num[x], plus, sub, mul - 1, div);
    if (div && num[x] != 0)
        dfs(x + 1, (int)temp / num[x], plus, sub, mul, div - 1);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num[i];
    }
    for (int i = 0; i < 4; i++) {
        cin >> arr[i];
    }
    dfs(1, num[0], arr[0], arr[1], arr[2], arr[3]);
    cout << maxi << '\n' << mini;
    return 0;
}