/*

Maximum Amount of Gold
Given a set of gold bars of various weights and a backpack that can hold at most  W pounds, place as much gold as possible into the backpack.
Input:
A set of  n gold bars of integer weights  w[1], ..., w[n] and a backpack that can hold at most  W pounds.
Output:
A subset of gold bars of maximum total weight not exceeding  W.

Sample.
Input:
10 3
1 4 8
Output:
9

Sample Input 2:
20 4
5 7 12 18
Sample Output 2:
19

  0 1 2 3 4 5 6 7 8 9 10
0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 1 1 1 1 1 1 1 1 1
4 0 1 1 1 4 5 5 5 5 5 5
8 0 1 1 1 4 5 5 5 8 9 9

*/
#include<iostream>
#include<vector>

using std::vector;

int getMaxWeight (int backpackWeight, vector<int> &items) {
	vector<vector<int>> result;
	for (int i = 0; i <= items.size(); ++i) {
		result.push_back(vector<int>(backpackWeight + 1, 0));
	}

	for (int i = 1; i <= items.size(); ++i) {
		int item = items[i - 1];
		for (int w = 1; w <= backpackWeight; ++w ) {
			if (item > w) {
				result[i][w] = result[i - 1][w];
				continue;
			}
			result[i][w] = std::max(
				std::max(result[i][w - 1], result[i - 1][w]),
				item + result[i - 1][w - item]
			);

		}
	}

	return result[items.size()][backpackWeight];
}

int main () {
	int backpackWeight;
	int n;

	std::cin >> backpackWeight >> n;

	vector<int> items;
	for (int i = 0; i < n; ++i) {
		int item;
		std::cin >> item;
		items.push_back(item);
	}

	int maxWeight = getMaxWeight(backpackWeight, items);

	std::cout << maxWeight << '\n';

	return 0;
}