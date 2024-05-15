#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
using namespace std;

int n, k;
deque<int> belt;
deque<bool> robot;

void turn() {
    robot.push_front(robot.back());
    robot.pop_back();

    belt.push_front(belt.back());
    belt.pop_back();

    robot[n - 1] = false;
}

void move() {
    for (int i = n - 2; i >= 0; i--) {
        if (!robot[i + 1] && robot[i] && belt[i + 1] > 0) {
            robot[i + 1] = true;
            robot[i] = false;
            belt[i + 1]--;
        }
    }
    robot[n - 1] = false;
}

void up() {
    if (!robot[0] && belt[0] > 0) {
        robot[0] = true;
        belt[0]--;
    }
}

bool check() {
    int temp = 0;
    for (int i = 0; i < 2 * n; i++) {
        if (!belt[i]) temp++;
    }
    if (temp >= k) return false;
    else return true;
}

int main() {
    cin >> n >> k;
    for (int i = 0; i < 2*n; i++) {
        int a;
        cin >> a;
        belt.push_back(a);
        robot.push_back(false);
    } 
    int cnt = 0;
    while (1) {
        turn();
        move();
        up();
        cnt++;
        if (!check()) break;
    }
    cout << cnt;
    return 0;
}