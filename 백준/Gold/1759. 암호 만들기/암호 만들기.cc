#include <iostream>
#include <algorithm>
using namespace std;

int l, c;
char alphabet[16];


bool check(string p) {
	int x = 0, y = 0;
	for (int i = 0; i < p.length(); i++) {
		if (p[i] == 'a' || p[i] == 'e' || p[i] == 'i' || p[i] == 'o' || p[i] == 'u') x += 1;
		else y += 1;
	}
	if (x >= 1 && y >= 2) return true;
	else return false;

}

void dfs(int idx, string s) {
	if (s.length() == l) {
		if (check(s)) {
			cout << s << '\n';
		}
		return;
	}
	if (c == idx) return;
	dfs(idx + 1, s + alphabet[idx]);
	dfs(idx+1, s);
}

int main() {
	cin >> l >> c;
	for (int i = 0; i < c; i++) {
		cin >> alphabet[i];
	}
	sort(alphabet, alphabet + c);
	dfs(0, "");
	return 0;
}