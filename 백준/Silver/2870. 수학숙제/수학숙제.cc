#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

string ret;
vector<string> v;

void go() {
    while (true) {
        if (ret.size() && ret.front() == '0') //항상 size있나 확인 후 앞이 0이라면
            ret.erase(ret.begin());//지워주기
        else break; //다 지웠으면 break
    }
    if (ret.size() == 0) ret = "0"; //0000이면 다 지워졌을거니 0하나만 더해주기
    v.push_back(ret);
    ret = "";
}

bool cmp(string a, string b) {
    if (a.size() == b.size()) return a < b; //사이즈 같으면 더 큰 수가 뒤로 return
    return a.size() < b.size(); //사이즈가 더 큰게 뒤로 return
}
int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        ret = "";
        for (int j = 0; j < s.length(); j++) {
            if (s[j] < 65) ret += s[j]; //숫자 판별
            else if (ret.size()) go(); //0일 경우
        }
        if (ret.size()) go(); //0남았는지 판별
    }
    sort(v.begin(), v.end(), cmp); //cmp없으면 20 ,123 중 제일 앞 2가 크니 20이 더 크다고 해버림
    for (string i : v)
        cout << i << '\n';
    return 0;

}