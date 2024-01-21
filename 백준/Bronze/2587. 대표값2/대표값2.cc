#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    vector<int> v(5);
    int sum = 0, cnt = 0;
    for (int i = 0; i < 5; i++) {
        cin >> v[i];
        sum += v[i];
        cnt++;
    }
    sort(v.begin(), v.end());
    int avg = sum / cnt;
    cout << avg << endl << v[2];
    return 0;
}