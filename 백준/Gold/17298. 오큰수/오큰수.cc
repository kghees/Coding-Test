#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;


int n;
int arr[1000001];
int dat[1000001];
vector<int> st;
int main() {
	cin >> n;
	memset(dat, -1, sizeof(dat));
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		while (st.size() && arr[st.back()] < arr[i]) {
			dat[st.back()] = arr[i];
			st.pop_back();
		}
		st.push_back(i);
	}
	for (int i = 0; i < n; i++)
		cout << dat[i] << " ";
	return 0;
}