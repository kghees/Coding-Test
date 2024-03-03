#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


bool yes(char x) {
    if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') return true;
    return false;
}

int main() {
    while (true) {
        string s;
        cin >> s;
        if (s == "end") break;
        // a : 연속모음의 개수, b : 연속자음의 개수, v : 모음 확인
        int a = 0, b = 0, v = 0;
        char temp;
        bool check = false;
        for (int i = 0; i < s.length(); i++) {
            if (yes(s[i])) {
                a++;
                b = 0;
                v = 1;
            }
            else {
                a = 0;
                b++;
            }
            if (a == 3 || b == 3) check = true;
            if (i >= 1 && (temp == s[i]) && (s[i] != 'o' && s[i] != 'e'))
                check = true;
            temp = s[i];
        }
        if (v == 0) check = true;

        if (check) cout << "<" << s << "> " << "is not acceptable.\n";
        else cout << "<" << s << "> " << "is acceptable.\n";
    }

}