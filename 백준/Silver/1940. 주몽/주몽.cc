#include <iostream>
using namespace std;
int n, m;
int arr[15001];
int res = 0;
int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == m) res++;
        }
    }
    cout << res;
    return 0;
}