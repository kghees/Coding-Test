#include<iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
vector<int> arr;
vector<int> temp;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		arr.push_back(a);
		temp.push_back(a);
	}
	sort(temp.begin(), temp.end());
	temp.erase(unique(temp.begin(), temp.end()), temp.end());

	for (int i = 0; i < n; i++) {
		cout << lower_bound(temp.begin(), temp.end(), arr[i]) - temp.begin() << " ";
	}
	
	return 0;
}