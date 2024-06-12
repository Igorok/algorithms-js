/*

Sample Input 1:
7
2 4 4 4 7 7 9
4
9 4 5 2
Sample Output 1:
6 1 -1 0

Sample Input 2:
8
1 2 3 4 5 6 7 8
8
1 2 3 4 5 6 7 8
Sample Output 2:
0 1 2 3 4 5 6 7

*/

#include <iostream>
#include <vector>

using std::vector;

int bin_search_ (vector<long long> &listValues, long long query) {
    int left = 0;
    int right = listValues.size() - 1;

    while (left <= right) {
        int middle = (int)((left + right) / 2);

        if (listValues[middle] == query) {
            int idx = middle;
            while (listValues[idx - 1] == query) {
                idx -= 1;
            }
            return idx;
        }

        if (query > listValues[middle]) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return -1;
}

int bin_search (vector<long long> &listValues, long long query) {
    int left = 0;
    int right = listValues.size() - 1;
    int idx = -1;

    while (left <= right) {
        int middle = (int)((left + right) / 2);

        if (listValues[middle] == query) {
            idx = middle;
            right = middle - 1;
        }

        if (query > listValues[middle]) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return idx;
}


int main () {
    int n;
    int m;
    vector<long long> listN;
    vector<long long> listM;

    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int val;
        std::cin >> val;
        listN.push_back(val);
    }

    std::cin >> m;
    for (int i = 0; i < m; ++i) {
        int val;
        std::cin >> val;
        int idx = bin_search(listN, val);
        std::cout << idx << " ";
    }
    std::cout << "\n";

    return 0;
}
