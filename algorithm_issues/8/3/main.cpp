/*

Primitive Calculator
Find the minimum number of operations needed to get a positive integer n from 1
by using only three operations: add 1, multiply by 2, and multiply by 3.
Input:
An integer n.
Output:
The minimum number of operations "+1", "*2", and "*3" needed to get n from 1.

Sample 1.
Input:
1
Output:
0
1

Sample 2.
Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234

Sample Input 1:
1
Sample Output 1:
0
1

Sample Input 2:
5
Sample Output 2:
3
1 2 4 5

*/

#include <iostream>
#include <vector>

using std::vector;

void print_calculated_path (int n) {
	vector<int> allOperations(n + 1, n * 10);
	vector<int> allPath(n + 1, -1);
	allOperations[0] = 0;
	allOperations[1] = 0;

	for (int i = 1; i <= n; ++i) {
		// +1
		int previous = i - 1;
		allOperations[i] = std::min(allOperations[i], allOperations[previous] + 1);
		allPath[i] = previous;

		// * 2
		previous = (int) i / 2;
		if (i % 2 == 0 && (allOperations[previous] + 1 < allOperations[i])) {
			allOperations[i] = allOperations[previous] + 1;
			allPath[i] = previous;
		}

		// * 3
		previous = (int) i / 3;
		if (i % 3 == 0 && (allOperations[previous] + 1 < allOperations[i])) {
			allOperations[i] = allOperations[previous] + 1;
			allPath[i] = previous;
		}
	}
	std::cout << allOperations[n] << "\n";

	vector<int> currentPath;
	int item = n;
	while (item > 0) {
		currentPath.push_back(item);
		item = allPath[item];
	}

	for (int i = currentPath.size() - 1; i >= 0; i--) {
		std::cout << currentPath[i] << " ";
	}
	std::cout << "\n";
}

int main () {
	int n;
	std::cin >> n;

	print_calculated_path(n);

	return 0;
}