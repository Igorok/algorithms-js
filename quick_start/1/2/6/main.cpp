/*
Give a sum of the segment.
Solution: if I know a sum of number for every item I can subtract the sum of the start from the sum of the end.

Sample Input:
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

Sample Output:
1
3
6
10
2
5
9
3
7
4

*/

#include<iostream>
#include<vector>

using std::vector;

int main () {
    int n;
    int q;

    std::cin >> n >> q;

    vector<long long> numbers{0};
    vector<long long> sumOfNumbers{0};

    for (int i = 0; i < n; ++i) {
        long long val;
        std::cin >> val;

        numbers.push_back(val);
        sumOfNumbers.push_back(val + sumOfNumbers[i]);
    }

    for (int i = 0; i < q; ++i) {
        int start;
        int end;

        std::cin >> start >> end;

        std::cout << sumOfNumbers[end] - sumOfNumbers[start - 1] << "\n";
    }

    return 0;
}
