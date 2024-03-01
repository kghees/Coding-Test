#include <iostream>
using namespace std;

int n, m, j,r;
int res = 0;
int main() {
    cin >> n >> m >> j;
    int l = 1; //시작지점
    for (int i = 0; i < j; i++) {
        int a;
        cin >> a;
        r = l + m - 1; //바구니 크기
        if (a >= l && a <= r) continue; 
        else {
            if (a < l) {
                res += (l - a);
                l = a;
            }
            else {
                l += (a - r);
                res += (a - r);
            }
        }
    }
    cout << res;
    return 0;
}