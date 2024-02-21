#include <iostream>
using namespace std;
long long a, b, c;
long long go(long long x, long long y) {
    if (y == 1) return x % c;

    long long ret = go(x, y / 2);
    ret = (ret * ret) % c;
    if (y % 2) ret = (ret * x) % c; // 홀수이면 2^5 = 2^4 * 2이므로 한번 더 곱해줘야함
    return ret;
}
int main() {
    cin >> a >> b >> c;
    cout << go(a, b) << '\n';
    return 0;
}