#include<iostream>
#include <algorithm>
using namespace std;

long long n;
long long num[2001];
long long cnt;

bool bs(long long tar, int idx) {
	long long st = 0;
	long long en = n - 1;
	long long mid = 0;

	while (st < en) {
		mid = num[st] + num[en];
		if (mid == tar) {
			if (st != idx && en != idx) return true;
			else if (st == idx) st += 1;
			else en -= 1;
		}

		else if (mid > tar) en -= 1;
		else st += 1;
	}
	return false;
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num[i];
	}
	sort(num, num + n);
	for (int i = 0; i < n; i++) {
		bool check = bs(num[i], i);
		if (check)cnt++;

	}
	cout << cnt;
	return 0;
}