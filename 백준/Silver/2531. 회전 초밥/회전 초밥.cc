#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int n, d, k, c;
int sushi[30001];

int main() {
    cin >> n >> d >> k >> c;
    for (int i = 0; i < n; i++) {
        cin >> sushi[i];
    }
    int st = 0;
    int en = k;
    int res = 0;
    int dat[3001] = { 0 };
    while (st <= en && st <= n) {
        memset(dat, 0, sizeof(dat));
        int cnt = 0;
        for (int i = st; i < en; i++) {
            if (dat[sushi[i % n]])continue;
            dat[sushi[i % n]] = 1;
            cnt++;
        }
        if (!dat[c])cnt++;
        res = max(res, cnt);
        st++;
        en++;
    }
    cout << res;
    return 0;
}