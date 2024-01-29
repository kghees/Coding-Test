#include <iostream>
#include <algorithm>
using namespace std;
int arr[11][11] = { 0 };
int t, n;
void print(int tc) {
	arr[0][0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j || j == 0)
				arr[i][j] = 1;
			else {
				arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
			}
		}
	}
	cout << "#" << tc+1 << '\n';
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			if (arr[i][j] != 0)
				cout << arr[i][j] << " ";
		}
		cout << '\n';
	}
}
int main() {
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		print(i);
	}

    return 0;
}
