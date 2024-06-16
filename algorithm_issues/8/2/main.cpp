/*

Money Change Again
Compute the minimum number of coins needed to change the given value into coins with denominations 1, 3, and 4.
Input:
An integer  money money.
Output:
The minimum number of coins with denominations  1, 3, and 4 that changes  money money.

Input:
34
Output:
9

Sample Input 1:
1
Sample Output 1:
1

Sample Input 2:
4
Sample Output 2:
1

34 = 4*8 + 1*2 = 10 coins
34 = 4*7 + 3*2 = 9 coins

*/

#include <iostream>
#include <vector>

using std::vector;

vector<int> coins = {4, 3, 1};

int get_change_greedy(int m) {
	int sum = 0;
	int money = m;

	for (int i = 0; i < coins.size(); ++i) {
		int count = (int) money / coins[i];

		std::cout << "coins[i] " << coins[i] << " count " << count << '\n';

		if (count != 0) {
			sum += count;
			money -= (count * coins[i]);

			std::cout << "sum " << sum << " money " << money << '\n';

			if (sum == m) {
				return sum;
			}
		}
	}

	return sum;
}

int get_change(int m) {
	vector<int> values(m + 1, m * 10);
	values[0] = 0;

	for (int i = 1; i <= m; ++i) {
		for (int j = 0; j < coins.size(); ++j) {
			int diff = i - coins[j];
			if (diff >= 0) {
				values[i] = std::min(values[diff] + 1, values[i]);
			}
		}
	}

	return values[m];
}

int main() {
	int m;
	std::cin >> m;
	std::cout << get_change(m) << '\n';
}