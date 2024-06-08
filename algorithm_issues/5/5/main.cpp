#include <iostream>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int fibonacci_sum_mod(long long n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;
    int sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % 10;
        sum = (sum + current) % 10;
    }

    return sum % 10;
}

void test () {
    for (int i = 0; i < 100; ++i) {
        int r1 = fibonacci_sum_naive(i);
        int r2 = fibonacci_sum_mod(i);
        if (r1 == r2) {
            std::cout << "OK: " << " i - " << i << " SUM: " << r1 << "\n";
        } else {
            std::cout << "ERROR: " << " i - " << i << " r1: " << r1 << " r2: " << r2 << "\n";
            break;
        }
    }
}


int main() {
//    test();

    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_mod(n) << "\n";
}
