/*

Edit Distance
Compute the edit distance between two strings.
Input:
Two strings.
Output:
The minimum number of single-symbol insertions, deletions, and substitutions to transform one string into the other one.

There are 3 actions: delete, insert, change. Every action is 1 operation.

Convert abc -> ""
  ""
  0
a 1
b 2
c 3
Walk through abc and delete every char
a = [i-1, j] + 1 = 1
b = [i-1, j] + 1 = 2
c = [i-1, j] + 1 = 3

Convert "" -> abc
     a b c
'' 0 1 2 3
add a = [i, j-1] + 1 = 1
add b = [i, j-1] + 1 = 2
add c = [i, j-1] + 1 = 3

Convert short -> ports
    p o r t s
  0 1 2 3 4 5
s 1
h 2
o 3
r 4
t 5
Walking through short
We already know operations:
add - [i, j-1] + 1
delete - [i-1, j] + 1
change - [i-1, j-1] + 1
equal - [i-1, j-1]

We will select minimum of this operations + 1

Sample 1.
Input:
short
ports
Output:
3

Sample 2.
Input:
editing
distance
Output:
5

Sample 3.
Input:
ab
ab
Output:
0

*/

#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;


int get_num_operations (string from, string to) {
	vector<vector<int>> operations;
	int maxVal = std::max(from.size(), to.size()) * 10;

	for (int i = 0; i <= from.size(); ++i) {
		operations.push_back(vector<int>(to.size() + 1, maxVal));
	}

	for (int i = 0; i <= from.size(); ++i) {
		operations[i][0] = i;
	}

	for (int j = 0; j <= to.size(); ++j) {
		operations[0][j] = j;
	}

	for (int i = 1; i <= from.size(); ++i) {
		for (int j = 1; j <= to.size(); ++j) {
			if (from[i-1] == to[j-1]) {
				operations[i][j] = operations[i - 1][j - 1];
				continue;
			}

			int dOperation = operations[i - 1][j] + 1;
			int aOperation = operations[i][j - 1] + 1;
			int cOperation = operations[i - 1][j - 1] + 1;

			operations[i][j] = std::min(std::min(dOperation, aOperation), cOperation);
		}
	}

	return operations[from.size()][to.size()];
}

int main () {
	string from;
	string to;

	std::cin >> from >> to;

	std::cout << get_num_operations(from, to) << "\n";

	return 0;
}
