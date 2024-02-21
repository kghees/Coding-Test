#include <iostream>
#include <vector>
using namespace std;
int n;
int cnt = 0;
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        vector<char> arr;
        for (int j = 0; j < s.length(); j++) {
            if (arr.empty() || arr.back() != s[j]) {
                arr.push_back(s[j]);
            }
            else {
                arr.pop_back();
            }
        }
        if (arr.empty()) cnt++;
    }
    cout << cnt;
    return 0;
}