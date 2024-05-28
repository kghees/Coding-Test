#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int t, h, w, n;
char map[21][21];
int y, x;
string command;
char d;

void init() {
    memset(map, ' ', sizeof(map));
}

void input() {
    cin >> h >> w;
    for (int i = 0; i < h; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++) {
            map[i][j] = s[j];
            if (s[j] == '^' || s[j] == 'v' || s[j] == '<' || s[j] == '>') {
                y = i, x = j;
                d = map[i][j];
            }
        }
    }
    cin >> n;
    cin >> command;
}

void shoot() {
    int dy = 0, dx = 0;
    if (d == '^') dy = -1;
    else if (d == 'v') dy = 1;
    else if (d == '<') dx = -1;
    else if (d == '>') dx = 1;

    int ny = y + dy, nx = x + dx;
    while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
        if (map[ny][nx] == '*') {
            map[ny][nx] = '.';
            break;
        }
        if (map[ny][nx] == '#') break;
        ny += dy;
        nx += dx;
    }
}

void move(char dir) {
    int dy = 0, dx = 0;
    if (dir == 'U') {
        dy = -1;
        d = '^';
    }
    else if (dir == 'D') {
        dy = 1;
        d = 'v';
    }
    else if (dir == 'L') {
        dx = -1;
        d = '<';
    }
    else if (dir == 'R') {
        dx = 1;
        d = '>';
    }

    int ny = y + dy, nx = x + dx;
    if (ny >= 0 && ny < h && nx >= 0 && nx < w && map[ny][nx] == '.') {
        map[y][x] = '.';
        y = ny;
        x = nx;
    }
    map[y][x] = d;
}

void battle() {
    for (char c : command) {
        if (c == 'S') shoot();
        else move(c);
    }
}

int main() {
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        init();
        input();
        battle();

        cout << "#" << tc + 1 << " ";
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                cout << map[i][j];
            }
            cout << '\n';
        }
    }
    return 0;
}
