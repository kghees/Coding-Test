#include <iostream>
#include <algorithm>
using namespace std;
int n, m;
int arr[500001];



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
        cout << upper_bound(arr, arr + n, x) - lower_bound(arr, arr + n, x) << " ";
    }

    return 0;
}