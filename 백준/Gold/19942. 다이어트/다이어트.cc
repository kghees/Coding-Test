#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
struct food {
    int protein;
    int province;
    int carbohydrate;
    int vitamin;
    int cost;
};

int n;
int mp, mf, ms, mv;
int dat[16];
vector<food> v;
int res = 1e9;
vector<int> ans;
int cnt = 0;

void dfs(int idx) {
    if (idx == v.size()) {
        int temp1 = 0, temp2 = 0, temp3 = 0, temp4 = 0;
        for (int i = 0; i < n; i++) {
            if (dat[i]) {
                temp1 += v[i].protein;
                temp2 += v[i].province;
                temp3 += v[i].carbohydrate;
                temp4 += v[i].vitamin;
            }
        }
        if (temp1 >= mp && temp2 >= mf && temp3 >= ms && temp4 >= mv) {
            int temp = 0;
            vector<int> a;
            for (int i = 0; i < n; i++) {
                if (dat[i]) {
                    temp += v[i].cost;
                    a.push_back(i + 1);
                }
            }
            if (res > temp || (res == temp && ans > a)) {
                res = temp;
                ans = a;
            }
        }
        return;
    }
    dat[idx] = 1;
    dfs(idx + 1);
    dat[idx] = 0;
    dfs(idx + 1);
}

int main() {
    cin >> n;
    cin >> mp >> mf >> ms >> mv;
    for (int i = 0; i < n; i++) {
        int a, b, c, d, e;
        cin >> a >> b >> c >> d >> e;
        v.push_back({ a,b,c,d,e });
    }

    dfs(0);

    if (res == 1e9) cout << -1;
    else {
        cout << res << '\n';
        for (int i : ans) cout << i << " ";
    }
    return 0;
}
