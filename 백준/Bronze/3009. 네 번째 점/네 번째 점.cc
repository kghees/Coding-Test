#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int arr[3], brr[3];
    for (int i = 0; i < 3; i++)
        cin >> arr[i] >> brr[i];
    if (arr[0] == arr[2])
        cout << arr[1] << " ";
    else if (arr[0] == arr[1])
        cout << arr[2] << " ";
    else
        cout << arr[0] << " ";
    if (brr[0] == brr[2])
        cout << brr[1];
    else if (brr[0] == brr[1])
        cout << brr[2];
    else
        cout << brr[0];
    return 0;
}