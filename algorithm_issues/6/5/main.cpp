#include<iostream>
#include<vector>
#include <algorithm>

using std::vector;

long long total_price (int n, vector<long long> prices, vector<long long> clicks) {
	std::sort(prices.begin(), prices.end(), std::greater<long long>());
	std::sort(clicks.begin(), clicks.end(), std::greater<long long>());
	long long total_price = 0;

	for (int i = 0; i < n; ++i) {
		total_price += prices[i] * clicks[i];
	}

	return total_price;
}

int main () {
	int n;
	vector<long long> prices;
	vector<long long> clicks;

	std::cin >> n;

	for (int i = 0; i < n; ++i) {
		long long p;
		std::cin >> p;
		prices.push_back(p);
	}

	for (int i = 0; i < n; ++i) {
		long long c;
		std::cin >> c;
		clicks.push_back(c);
	}

	std::cout << total_price(n , prices, clicks) << "\n";

	return 0;
}