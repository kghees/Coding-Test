#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int h, w;
char map[100][100];
int check[100][100];
int main() {
    cin >> h >> w;
    memset(check, -1, sizeof(check));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> map[i][j];
            if (map[i][j] == 'c') check[i][j] = 0;
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (check[i][j] == 0) continue;
            else if (j > 0 && check[i][j] == -1 && check[i][j - 1] != -1) {
                check[i][j] = check[i][j - 1] + 1;
            }

        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << check[i][j] << " ";
        }
        cout << '\n';
    }
    return 0;

}