#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;
    double sum = 0;
    cin >> n;
    double arr[1001];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    for (int i = 0; i < n; i++) {
        sum += (arr[i] / arr[n - 1]) * 100;
    }
    cout << sum / n;
    return 0;
}