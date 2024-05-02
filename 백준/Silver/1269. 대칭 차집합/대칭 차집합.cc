#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int a, b;

map<int, int> arr;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> a >> b;
	for (int i = 0; i < a+b; i++) {
		int x;
		cin >> x;
		if (arr[x] == 1) arr.erase(x);
		else arr[x] = 1;
	}
	cout << arr.size();
	return 0;
}