#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    while (true) {
        cin >> n;
        if (n == -1)
            break;
        vector<int> arr;
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                arr.push_back(i);
                sum += i;
            }
        }
        if (sum == n) {
            cout << n << " = ";
            for (int i = 0; i < arr.size() - 1; i++) {
                cout << arr[i] << " + ";
            }
            cout << arr[arr.size() - 1] << endl;
        }
        else
            cout << n << " is NOT perfect." << endl;
    }
    return 0;
}