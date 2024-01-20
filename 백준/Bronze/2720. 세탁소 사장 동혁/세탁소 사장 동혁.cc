#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int t, m;
    cin >> t;
    while (t--) {
        int q=0, d=0, n=0, p=0;
        cin >> m;
        while (m) {
            if (m >= 25) {
                q++;
                m -= 25;
            }
            else if (m >= 10) {
                d++;
                m -= 10;
            }
            else if (m >= 5) {
                n++;
                m -= 5;
            }
            else {
                p++;
                m -= 1;
            }
        }
        cout << q << " " << d << " " << n << " " << p << endl;
    }
    return 0;
}