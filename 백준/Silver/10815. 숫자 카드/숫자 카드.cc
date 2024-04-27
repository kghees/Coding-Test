#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m;
int arr[500001];

bool bs(int tar) {
    int st = 0;
    int en = n - 1;
    int mid = 0;

    while (st <= en) {
        mid = (st + en) / 2;

        if (arr[mid] == tar) return true;

        else if (arr[mid] < tar) st = mid + 1;
        else en = mid - 1;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (bs(x)) cout << 1 << " ";
        else cout << 0 << " ";
    }
    return 0;
}