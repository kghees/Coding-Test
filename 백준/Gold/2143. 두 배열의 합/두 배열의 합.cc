#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long t;
int n, m;
int a[1001], b[1001];
vector<int> a_prefix;
vector<int> b_prefix;
long long res;

int lowerBound(int tar) {
    int st = 0;
    int en = b_prefix.size();
    
    while (st < en) {
        int mid = (st + en) / 2;
        if (b_prefix[mid] < tar) st = mid + 1;
        else en = mid;
    }
    return st;
}

int upperBound(int tar) {
    int st = 0;
    int en = b_prefix.size();

    while (st < en) {
        int mid = (st + en) / 2;
        if (b_prefix[mid] <= tar) st = mid + 1;
        else en = mid;
    }
    return st;
}

int main() {
    cin >> t;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> m;
    for (int i = 0; i < m; i++) cin >> b[i];

    //a에서 나올 수 있는 모든 합 만들기
    for (int i = 0; i < n; i++) {
        int x = a[i];
        a_prefix.push_back(x);
        for (int j = i + 1; j < n; j++) {
            x += a[j];
            a_prefix.push_back(x);
        }
    }
    //b에서 나올 수 있는 모든 합 만들기
    for (int i = 0; i < m; i++) {
        int x = b[i];
        b_prefix.push_back(x);
        for (int j = i + 1; j < m; j++) {
            x += b[j];
            b_prefix.push_back(x);
        }
    }
    sort(b_prefix.begin(), b_prefix.end());
    for (int i = 0; i < a_prefix.size(); i++) {
        int temp = t - a_prefix[i];
        long long lb = lowerBound(temp);
        long long ub = upperBound(temp);
        res += (ub - lb);
    }
    cout << res;
    return 0;
}