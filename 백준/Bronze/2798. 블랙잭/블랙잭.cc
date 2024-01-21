#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, m,a;
    cin >> n >> m;
    vector<int> arr;
    for (int i = 0; i < n; i++) {
        cin >> a;
        arr.push_back(a);
    }
    int max = 0;
    for (int i = 0; i < arr.size() - 2; i++) {
        int sum = 0;
        for (int j = i + 1; j < arr.size() - 1; j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                sum = arr[i] + arr[j] + arr[k];
                if (sum <= m && max < sum) {
                    max = sum;
                }
            }
        }
    }
    cout << max;
    return 0;
}