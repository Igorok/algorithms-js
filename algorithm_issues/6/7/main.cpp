/*

Output format. In the first line, output the maximum number k such that n can be represented as the sum of k pairwise distinct positive integers. In the second line, output k pairwise distinct positive integers that sum up to n (if there are multiple such representations, output any of them).

Input:
6
Output:
3
1 2 3

Sample 2.
Input:
8
Output:
3
1 2 5

Sample 3.
Input:
2
Output:
1 2

---

1 2 3 4 5 6
7 7 7
(a[0] + a[5]) * (6 / 2)

21

x * (x + 1) / 2
x * (x + 1) / 2 = 21
x * (x + 1) = 42
x^2 + x - 42 = 0

ax^2 + by + c = 0
D = b^2 - 4ac
x = (-b + D^(1/2)) / 2a

D = 1 - 4 * -42 =  169
x = (-1 + 13) / 2 = 6

x - count of numbers


k*(k+1)/2 <= n;
b = n - k*(k+1)/2 >= 0

*/

#include <iostream>
#include <vector>

using std::vector;

bool is_valid (long long k, long long n) {
    return k * (k + 1) / 2 <= n;
}

vector<long long> optimal_summands(long long n) {
    if (n < 2) return {n};

    vector<long long> summands;
    long long sum = 0;
    for (long long i = 1; i < n; ++i) {
        if (!is_valid(i, n)) {
            break;
        }
        sum += i;
        summands.push_back(i);
    }

    int s = summands.size();
    if (s != 0 && sum != n) {
        summands[s - 1] = summands[s - 1] + (n - sum);
    }

    return summands;
}

int main() {
    long long n;
    std::cin >> n;
    vector<long long> summands = optimal_summands(n);

    std::cout << summands.size() << '\n';
    for (size_t i = 0; i < summands.size(); ++i) {
        std::cout << summands[i] << ' ';
    }
    std::cout << "\n";
}
