/*

Sample.
Input:
34
Output:
9

34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4

*/

#include<iostream>
#include<vector>

using std::vector;

vector<int> coins = { 1, 3, 4 };

int getCoinsCount (int n) {
    vector<int> coinsCount(n + 1, 10e4);
    coinsCount[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < coins.size(); ++j) {
            int prevSum = i - coins[j];

            if (prevSum >= 0) {
                coinsCount[i] = std::min(
                    coinsCount[i],
                    coinsCount[prevSum] + 1
                );
            }
        }
    }

    return coinsCount[n];
}

int main () {
    int n;
    std::cin >> n;

    std::cout << getCoinsCount(n) << "\n";

    return 0;
}
