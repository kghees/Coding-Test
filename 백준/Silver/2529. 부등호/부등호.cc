#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int k;
int dat[10];
char arr[10];
vector<string> res;

bool check(char x, char y, char op) {
    //부등호에 맞게 들어왔으면 true
    if (x < y && op == '<') return true; 
    if (x > y && op == '>') return true;
    return false; //그게 아니라면 false
}

void dfs(int x, string s) {
    //k+1자리 만들었으면 vector에 모두 넣어주기
    if (x == k + 1) {
        res.push_back(s);
        return;
    }
    for (int i = 0; i < 10; i++) {
        if (dat[i]) continue; //이미 쓴 거는 continue
        //첫번째는 그냥 넣어주고 나머지는 부등호 판단해서 넣어주기
        if (x == 0 || check(s[x - 1], i + '0', arr[x - 1])) { //숫자 문자로 넣어주기!
            dat[i] = 1; //쓴 거 체크
            dfs(x + 1, s + to_string(i)); //문자열로 바꿔서 넣어주기
            dat[i] = 0; // 다른 경우 위해 쓴 거 체크 해제
        }
    }
}

int main() {
    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> arr[i];
    }
    dfs(0, "");
    sort(res.begin(), res.end()); //가장 큰값과 작은값 위해 정렬
    cout << res[res.size()-1] << '\n' << res[0];
    return 0;
}