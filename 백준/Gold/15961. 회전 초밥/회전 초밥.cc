#include <iostream>
#include <algorithm>
using namespace std;

int n, d, k, c;
int sushi[3000001];
int dat[3004];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> d >> k >> c;
    for (int i = 0; i < n; i++) {
        cin >> sushi[i];
    }
    int res = 0,cnt = 0;
    int st = 0;
    int en = k-1;
    for (int i = 0; i < k; i++) {
        if (!dat[sushi[i]]) {
            cnt++;
        }
        dat[sushi[i]]++;
    }
    if (!dat[c]) res = max(res, cnt + 1);
    else res = max(res, cnt);

    while (true) {
        dat[sushi[st]]--;
        if (!dat[sushi[st % n]]) cnt--;
        st++;
        if (st == n) break;

        en++;
        if (!dat[sushi[en % n]]) cnt++;
        dat[sushi[en % n]]++;

        if (!dat[c]) res = max(res, cnt + 1);
        else res = max(res, cnt);
    }
    cout << res;
    return 0;
}