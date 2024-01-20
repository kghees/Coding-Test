#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    string s,t; double res = 0,resgrade = 0;
    double score[20], grade[20];
    for (int i = 0; i < 20; i++) {
        cin >> s >> grade[i] >> t;
        if (t == "A+") score[i] = 4.5;
        else if (t == "A0") score[i] = 4.0;
        else if (t == "B+") score[i] = 3.5;
        else if (t == "B0") score[i] = 3.0;
        else if (t == "C+") score[i] = 2.5;
        else if (t == "C0") score[i] = 2.0;
        else if (t == "D+") score[i] = 1.5;
        else if (t == "D0") score[i] = 1.0;
        else if (t == "F") score[i] = 0.0;
        else if (t == "P") { score[i] = 0.0; grade[i] = 0.0; }
        res += (score[i] * grade[i]);
        resgrade += grade[i];
    }
    res /= resgrade;
    cout << fixed;
    cout.precision(6);
    cout << res;
    return 0;
}