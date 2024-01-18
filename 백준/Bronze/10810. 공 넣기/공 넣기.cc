#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int arr[101] = { 0 };
    int x, y, z;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> z;
        for (int j = x; j <= y; j++) {
            arr[j] = z;
        }
    }
    for (int i = 1; i < n+1; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}