#include <iostream>
#include <algorithm>
using namespace std;

int t;

int gcd(int a, int b) {
	int r;
	while (1) {
		int r = a % b;

		if (r == 0) return b;
		a = b;
		b = r;
	}
}

int lcm(int a, int b) {
	return a * b / gcd(a, b);
}

int main() {
	cin >> t;
	for (int i = 0; i < t; i++) {
		int a, b;
		cin >> a >> b;
		cout << lcm(a, b) << '\n';
	}

	return 0;
}
