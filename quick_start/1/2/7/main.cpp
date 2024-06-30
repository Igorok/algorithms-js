/*

Sample Input 1:
4
1 2 3 4

Sample Output 1:
10

Sample Input 2:
4
5 4 -10 4
Sample Output 2:
9


4
-4 5 4 -10
*/

#include<iostream>

int main () {
    int n;
    std::cin >> n;

    long long sum;
    std::cin >> sum;

    long long max = sum;

    for (int i = 1; i < n; ++i) {
        long long val;
        std::cin >> val;

        if (sum < val && sum + val < val) {
            sum = val;

            if (max < sum) {
                max = sum;
            }

            continue;
        }

        sum += val;
        if (max < sum) {
            max = sum;
        }
    }

    std::cout << max << "\n";

    return 0;
}
