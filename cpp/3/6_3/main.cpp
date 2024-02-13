#include <iostream>
using namespace std;


int main () {
    int i = 3;
    int j = 10;
    int const ** m = new int * [i];

    for (int idx = 0; idx < i; idx++) {
        m[idx] = new int[j];
        for (int n = 0; n < j; n++) {
            m[idx][n] = n;
        }
    }

    for (int idx = 0; idx < i; idx++) {
        for (int n = 0; n < j; n++) {
            cout << m[idx][n] << " ";
        }
        cout << endl;
    }
    return 0;
};
