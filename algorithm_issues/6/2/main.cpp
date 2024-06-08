#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

vector<int> coins = {1, 5, 10};

int getCoins (int amount) {
    if (amount < 2) {
        return amount;
    }
    std::sort(coins.begin(), coins.end(), std::greater<int>());

    int count = 0;
    for (int i = 0; i < coins.size(); ++i) {
        auto divResut = std::div(amount, coins[i]);
        count += divResut.quot;
        amount = divResut.rem;
    }

    return count;
}

int main() {
    int amount = 0;
    std::cin >> amount;

    int c = getCoins(amount);

    std::cout << c << "\n";

    return 0;
}
