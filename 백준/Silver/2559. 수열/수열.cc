#include <iostream>
#include <algorithm>
using namespace std;
int n, k;
int res = -10000001; // -100*(10만번)
int psum[1000001];
int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        psum[i] = psum[i - 1] + x; //누적합 구하기
    }
    for (int i = k; i <= n; i++) { //k개부터
        res = max(res, psum[i] - psum[i - k]); //연속적 k개합 최대 구하기
    }
    cout << res;
    return 0;
}
