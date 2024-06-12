/*

Sample Input 1:
5
1 5 8 12 13
5
8 1 23 1 11
Sample Output 1:
2 0 -1 0 -1

Sample Input 2:
10
2 3 4 5 6 7 8 9 10 11
12
1 2 3 4 5 6 7 8 9 10 11 12
Sample Output 2:
-1 0 1 2 3 4 5 6 7 8 9 -1

*/

#include <iostream>
#include <vector>

using std::vector;

int bin_search (vector<long long> &listValues, long long query) {
    int left = 0;
    int right = listValues.size() - 1;

    while (left <= right) {
        int middle = (int)((left + right) / 2);

        if (listValues[middle] == query) {
            return middle;
        }

        if (query > listValues[middle]) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return -1;
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
