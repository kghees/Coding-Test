#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int arr[31] = { 0 };
    int n;
    for (int i = 0; i < 28; i++) {
        cin >> n;
        arr[n] = 1;
    }
    for (int i = 1; i < 31; i++) {
        if (arr[i] == 0)
            cout << i << endl;
    }
    return 0;
}