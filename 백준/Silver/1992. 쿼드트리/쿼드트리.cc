#include <iostream>
#include <algorithm>
using namespace std;

int n;
string s;
char a[101][101];

string quard(int y, int x, int size) {
    if (size == 1) return string(1, a[y][x]); // char형을 string형으로 바꿔서
    char b = a[y][x];
    string ret = "";
    bool flag = 0;
    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (b != a[i][j]) {
                ret += '(';
                ret += quard(y, x, size / 2); //왼쪽 위
                ret += quard(y, x + size / 2, size / 2); //오른쪽 위
                ret += quard(y + size / 2, x, size / 2); //왼쪽 아래
                ret += quard(y + size / 2, x + size / 2, size / 2); //오른쪽 아래
                ret += ')';
                return ret;
            }
        }
    }
    return string(1, a[y][x]);//다 같으면 1 or 0 return
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < n; j++) {
            a[i][j] = s[j];
        }
    }
    cout << quard(0, 0, n) << '\n';
    return 0;
}