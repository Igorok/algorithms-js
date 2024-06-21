/*

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

1 2 6 7 21 22 66 198 594 1782 5346 16038 16039 32078 96234

*/

#include<iostream>
#include<vector>

using std::vector;

void printAnswer(long long n) {
    vector<long long> prevs(n + 1);
    vector<long long> operations(n + 1, n + 10);

    prevs[0] = 0;
    prevs[1] = 0;
    operations[0] = 0;
    operations[1] = 0;

    for (int i = 2; i <= n; ++i) {
        long long pn = i - 1;
        if (operations[pn] + 1 < operations[i]) {
            operations[i] = operations[pn] + 1;
            prevs[i] = pn;
        }

        if (i % 3 == 0) {
            long long pn = i / 3;
            if (operations[pn] + 1 < operations[i]) {
                operations[i] = operations[pn] + 1;
                prevs[i] = pn;
            }
        }
        if (i % 2 == 0) {
            long long pn = i / 2;
            if (operations[pn] + 1 < operations[i]) {
                operations[i] = operations[pn] + 1;
                prevs[i] = pn;
            }
        }
    }

    std::cout << operations[n] << "\n";

    long long prev = n;
    vector<long long> path;
    while (prev != 0) {
        path.push_back(prev);
        prev = prevs[prev];
    }

    for (long long i = path.size() - 1; i >= 0; --i) {
        std::cout << path[i] << " ";
    }
    std::cout << "\n";
}

int main () {
    long long n;
    std::cin >> n;

    printAnswer(n);

    return 0;
}
