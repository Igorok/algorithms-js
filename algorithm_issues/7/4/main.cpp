/*

Input format.
The first line contains an integer n, the next one contains a sequence of n non-negative integers. a[0], ..., a[n−1].
Output format.
Output 1 if the sequence contains an element that appears more than n/2 times, and 0 otherwise.

Input:
5
2 3 9 2 2
Output:
1

Input:
4
1 2 3 1
Output:
0


*/

#include<iostream>
#include <map>
#include<string>

using std::map;

int main () {
    int n;
    std::cin >> n;

    int halfN = n / 2;
    int result = 0;

    map<long long, int> countMap;

    for (int i = 0; i < n; ++i) {
        long long val;
        std::cin >> val;

        if (countMap.find(val) != countMap.end()) {
            if (countMap[val] + 1 > halfN) {
                result = 1;
                break;
            }

            countMap[val] += 1;
        } else {
            countMap[val] = 1;
        }
    }

    std::cout << result << "\n";

    return 0;
}
