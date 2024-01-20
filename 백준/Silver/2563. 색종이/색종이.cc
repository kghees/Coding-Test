#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int arr[100][100] = {0};
    int n, x, y, res = 0;
    cin >> n;
    while (n--) {
        cin >> x >> y;
        for (int i = x; i < x + 10; i++) {
            for (int j = y; j < y + 10; j++) {
                if (arr[i][j] == 0) {
                    arr[i][j] = 1;
                    res++;
                }
            }
        }
    }
    cout << res;
    return 0;
}