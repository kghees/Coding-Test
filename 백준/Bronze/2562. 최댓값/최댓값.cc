#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int a,max = 0, cnt = 0;
    for (int i = 0; i < 9; i++) {
        cin >> a;
        if (max < a) {
            max = a;
            cnt = i;
        }
    }
    cout << max << endl << cnt+1;
    return 0;
}