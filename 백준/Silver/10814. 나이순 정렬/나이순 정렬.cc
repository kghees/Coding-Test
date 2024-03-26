#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool cmp(pair<int, string> a, pair<int, string> b) {
    return a.first < b.first;
}

int n;

int main() {
    cin >> n;
    pair<int, string> a;
    vector<pair<int, string>> arr;
    for (int i = 0; i < n; i++) {
        cin >> a.first >> a.second;
        arr.push_back(a);
    }
    stable_sort(arr.begin(), arr.end(), cmp);
    for (int i = 0; i < n; i++) {
        cout << arr[i].first << " " << arr[i].second << '\n';
    }
    return 0;
}