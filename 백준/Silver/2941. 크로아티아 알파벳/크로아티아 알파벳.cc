#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<string> c = { "c=", "c-","dz=","d-","lj","nj","s=","z="};
    int cnt;
    string s;
    cin >> s;
    for (int i = 0; i < c.size(); i++) {
        while (true) {
            cnt = s.find(c[i]);
            if (cnt == string::npos)
                break;
            s.replace(cnt, c[i].length(),"#");
        }
    }
    cout << s.length();
    return 0;
}