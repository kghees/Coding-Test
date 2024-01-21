#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> res;
    vector<string> arr(n);
    string s;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < n - 7; i++) {
        for (int j = 0; j < m - 7; j++) {
            int cnt = 0, cnt1 = 0;
            for (int k = i; k < i + 8; k++) {
                for (int l = j; l < j + 8; l++) {
                    if ((k + l) % 2 == 0) {
                        if (arr[k][l] != 'W')
                            cnt++;
                        else
                            cnt1++;
                    }
                    else {
                        if (arr[k][l] != 'B')
                            cnt++;
                        else
                            cnt1++;
                    }
                }
            }
            res.push_back(min(cnt, cnt1));
        }
    }
    sort(res.begin(), res.end());
    cout << res[0];
    return 0;
}