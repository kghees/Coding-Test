#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int n;
vector<int> arr;
int dat[1000001];
vector<int> st;
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		arr.push_back(a);
	}
	st.push_back(0);
	for (int i = 1; i < n; i++) {
		if (st.empty()) st.push_back(i);

		while (!st.empty() && arr[st.back()] < arr[i]) {
			dat[st.back()] = arr[i];
			st.pop_back();
		}
		st.push_back(i);
	}
	while (!st.empty()) {
		dat[st.back()] = -1;
		st.pop_back();
	}
	for (int i = 0; i < n; i++) {
		cout << dat[i] << " ";
	}
	return 0;
}