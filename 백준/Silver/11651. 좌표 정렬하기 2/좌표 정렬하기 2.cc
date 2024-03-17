#include <iostream>
#include <algorithm>
using namespace std;
struct Point {
	int x, y;
};

bool cmp(Point a, Point b) {
	if (a.y == b.y) return a.x < b.x;
	return a.y < b.y;
}

int n;

int main() {
	cin >> n;
	Point arr[100001];
	for (int i = 0; i < n; i++) {
		cin >> arr[i].x >> arr[i].y;
	}

	sort(arr,arr+n,cmp);
	for (int i = 0; i < n; i++) {
		cout << arr[i].x << " " << arr[i].y << '\n';
	}
	return 0;
}