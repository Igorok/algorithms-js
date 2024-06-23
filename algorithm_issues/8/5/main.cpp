/*

Longest Common Subsequence of Two Sequences
Compute the maximum length of a common subsequence of two sequences.
Input:
Two sequences.
Output:
The maximum length of a common subsequence.

Sample 1.
Input:
3
2 7 5
2
2 5
Output:
2

Sample 2.
Input:
1
7
4
1 2 3 4
Output:
0

Sample 3.
Input:
4
2 7 8 3
4
5 2 8 7
Output:
2

Sample Input 1:
3
1 2 3
3
3 2 1
Sample Output 1:
1

Sample Input 2:
3
2 3 9
4
2 9 7 8
Sample Output 2:
2

*/

#include<iostream>
#include<vector>

using std::vector;

/*
1 10 2 11 3 12 4 13 5 6
*/
void findSingleSubsequence (vector<long long> sequence) {
	vector<int> length(sequence.size() + 1, 1);
	vector<int> previous(sequence.size() + 1, -1);
	int maxLength = 1;
	int lastId = 0;

	for (int i = 0; i < sequence.size(); ++i) {
		for (int j = 0; j < i; ++j) {
			if (sequence[i] > sequence[j] && length[i] < length[j] + 1) {
				length[i] = length[j] + 1;
				previous[i] = j;
			}
			if (length[i] > maxLength) {
				maxLength = length[i];
				lastId = i;
			}
		}
	}

	std::cout << maxLength << "\n";

	while (lastId != -1) {
		std::cout << sequence[lastId] << " ";
		lastId = previous[lastId];
	}
	std::cout << "\n";
}


/*
    1 2 3 4 5 6
  0 0 0 0 0 0 0
1 0 1 1 1 1 1 1
3 0 1 1 2 2 2 2
5 0 1 1 2 2 3 3
7 0 1 1 2 2 3 3
*/
void findCommonSubsequence (vector<long long> first, vector<long long> second) {
	vector<vector<long long>> result;
	for (int i = 0; i <= first.size(); ++i) {
		result.push_back(vector<long long>(second.size() + 1, 0));
	}

	for (int i = 1; i <= first.size(); ++i) {
		long long a = first[i - 1];
		for (int j = 1; j <= second.size(); ++j) {
			long long b = second[j - 1];
			result[i][j] = std::max(result[i - 1][j], result[i][j - 1]);
			// a == b; I can't take value from them
			if (a == b) {
				result[i][j] = std::max(result[i][j], result[i-1][j-1] + 1);
			}
		}
	}

	std::cout << result[first.size()][second.size()] << "\n";
}

int main () {
	int n;
	int m;
	vector<long long> first;
	vector<long long> second;

	std::cin >> n;
	for (int i = 0; i < n; ++i) {
		int v;
		std::cin >> v;
		first.push_back(v);
	}

	std::cin >> m;
	for (int i = 0; i < m; ++i) {
		int v;
		std::cin >> v;
		second.push_back(v);
	}

	findCommonSubsequence(first, second);

	return 0;
}