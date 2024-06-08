/*
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
0 1 1 2 3 0 3  3  1  4 0  4    4 3   2   0
*/

#include <iostream>
#include <vector>

using std::vector;

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % m;
    }

    return current % m;
}

vector<long long> memo;

long long pisano_period (long long n, long long m) {
    long long current = 0;
    long long next = 1;
    long long period = 0;
    
    memo = {};

    while (true) {
        memo.push_back(current);
    
        long long oldNext = next;
        next = (current + next) % m;
        current = oldNext;
        period += 1;
                
        if (current == 0 and next == 1) {
            return period;
        }
        if (period > n) {
            return period;
        }
    }
}

long long get_fibonacci_huge_pisano(long long n, long long m) {
    if (n <= 1)
        return n;

    long long period = pisano_period(n, m);
    long long remainder = n % period;

    return memo[remainder];
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    
//    std::cout << get_fibonacci_huge_naive(n, m) << '\n';
    std::cout << get_fibonacci_huge_pisano(n, m) << '\n';
    
//    for (long long i = 0; i < memo.size(); ++i) {
//        std::cout << memo[i] << " ";
//    }
//    std::cout << "\n";
}


