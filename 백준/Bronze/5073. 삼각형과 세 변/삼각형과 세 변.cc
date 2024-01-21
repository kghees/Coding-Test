#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    while (true) {
        cin >> a >> b >> c;
        int x = max(a, max(b, c));
        if (a == 0 && b == 0 && c == 0)
            break;
        if ((a + b + c) - x <= x)
            cout << "Invalid" << endl;
        else if (a == b && b == c)
            cout << "Equilateral" << endl;
        else if (a == b || b == c || a == c)
            cout << "Isosceles" << endl;
        else if (a != b && b != c && a != c)
            cout << "Scalene" << endl;
    }
    return 0;
}