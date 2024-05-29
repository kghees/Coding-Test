#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
struct Person {
    int num;
    int arrive_num;
    int reception_num;
    int repair_num;
};

struct Receptiondesk {
    Person person;
    int processing_time = -1;
    int complete_time = -1;
};

struct Repairdesk {
    Person person;
    int processing_time = -1;
    int complete_time = -1;
};

int t, n, m, k, a, b;
Person people[1001];
Receptiondesk receptions[10];
Repairdesk repairs[10];
queue<Person> q1, q2;

void input() {
    cin >> n >> m >> k >> a >> b;
    for (int i = 1; i <= n; i++) {
        cin >> receptions[i].processing_time;
    }
    for (int i = 1; i <= m; i++) {
        cin >> repairs[i].processing_time;
    }
    for (int i = 1; i <= k; i++) {
        people[i].num = i;
        cin >> people[i].arrive_num;
    }
}

void solution() {
    int now_time = 0;
    int out_count = 0;

    while (true) {
        //1.사람이 도착하면 접수 창구 대기 queue
        for (int i = 1; i <= k; i++) {
            if (people[i].arrive_num == now_time) {
                q1.push(people[i]);
            }
        }

        //2.접수 창구에서 작업이 끝난 사람은 정비 창구 대기 queue
        for (int i = 1; i <= n; i++) {
            if (receptions[i].complete_time == now_time) {
                q2.push(receptions[i].person);
                receptions[i].complete_time = -1;
            }
        }

        //3.접수 창구가 비어있는 지 체크
        //비어있다면 추가
        for (int i = 1; i <= n; i++) {
            if (q1.empty()) break;

            if (receptions[i].complete_time == -1) {
                receptions[i].complete_time = receptions[i].processing_time + now_time;
                receptions[i].person = q1.front();
                people[q1.front().num].reception_num = i;
                q1.pop();
            }
        }
        
        //4.정비 창구에서 작업이 끝난 사람은 내보내기
        for (int i = 1; i <= m; i++) {
            if (repairs[i].complete_time == now_time) {
                repairs[i].complete_time = -1;
                out_count++;
            }
        }

        //5.정비 창구가 비어있는 지 체크
        //비어있다면 추가
        for (int i = 1; i <= m; i++) {
            if (q2.empty()) break;

            if (repairs[i].complete_time == -1) {
                repairs[i].complete_time = repairs[i].processing_time + now_time;
                repairs[i].person = q2.front();
                people[q2.front().num].repair_num = i;
                q2.pop();
            }
        }
        now_time++;
        if (out_count == k) break;
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        input();
        solution();

        int res = 0;
        for (int i = 1; i <= k; i++) {
            if (people[i].reception_num == a && people[i].repair_num == b) {
                res += people[i].num;
            }
        }
        if (res == 0) cout << "#" << tc + 1 << " " << -1 << '\n';
        else cout << "#" << tc + 1 << " " << res << '\n';
    }
    return 0;
}
