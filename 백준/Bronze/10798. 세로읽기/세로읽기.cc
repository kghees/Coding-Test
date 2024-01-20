#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    char arr[15][15] = {0};
    string s;
    for (int i = 0; i < 5; i++) {
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            arr[i][j] = s[j];
        }
    }
    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 15; j++) {
            if (arr[j][i] != 0)
                cout << arr[j][i];
        }
    }
    return 0;
}