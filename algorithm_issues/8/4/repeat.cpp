/*

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


""->"asd" Add [i][j - 1] + 1
    a s d
- 0 1 2 3

"asd"->"" Delete [i-1][j] + 1
  -
  0
a 1
s 2
d 3

"aaa"->"bbb" Change [i-1][j-1] + 1
    a a a
  0 1 2 3
b 1 1 2 3
b 2 2 2 3
b 3 3 3 3

"aaa"->"aaa" [i-1][j-1]
    a a a
  0 1 2 3
a 1 0 1 2
a 2 1 0 1
a 3 2 1 0


*/

#include<iostream>
#include<vector>
#include<string>

using std::string;
using std::vector;

int getDiff (string from, string to) {
    vector<vector<int>> operations;

    for (int i = 0; i <= from.size(); ++i) {
        operations.push_back(vector<int>(to.size() + 1, 10e6));
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

            long long a = operations[i][j - 1] + 1;
            long long d = operations[i - 1][j] + 1;
            long long c = operations[i - 1][j - 1] + 1;

            operations[i][j] = std::min(std::min(a, d), c);
        }
    }

    return operations[from.size()][to.size()];
}

void test () {
    long long d = getDiff("", "asd");
    std::cout << (d == 3 ? "SUCCESS " : "ERROR ") << d << "\n";

    d = getDiff("asd", "");
    std::cout << (d == 3 ? "SUCCESS " : "ERROR ") << d << "\n";

    d = getDiff("aaa", "bbb");
    std::cout << (d == 3 ? "SUCCESS " : "ERROR ") << d << "\n";

    d = getDiff("aaa", "aaa");
    std::cout << (d == 0 ? "SUCCESS " : "ERROR ") << d << "\n";
};


int main () {
    string from;
    string to;

    std::cin >> from >> to;

//    test();

    std::cout << getDiff(from, to) << "\n";

    return 0;
}
