#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	for (int t = 0; t < 10; t++) {
		int n,n1;
		cin >> n;
		vector<int> arr;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			arr.push_back(a);
		}
		cin >> n1;
		for (int i = 0; i < n1; i++) {
			char s;
			int x, y;
			cin >> s >> x >> y;
			vector<int> temp;
			for (int j = 0; j < y; j++) {
				int num;
				cin >> num;
				temp.push_back(num);
			}
			arr.insert(arr.begin() + x, temp.begin(), temp.end());
		}
		cout << "#" << t + 1 << " ";
		for (int i = 0; i < 10; i++)
			cout << arr[i] << " ";
		cout << '\n';
	}
    return 0;
}
