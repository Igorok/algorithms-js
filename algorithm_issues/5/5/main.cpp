#include <iostream>
#include <vector>

using std::vector;

/*
%10
OK:  i - 0 SUM: 0
OK:  i - 1 SUM: 1
OK:  i - 2 SUM: 2
OK:  i - 3 SUM: 4
OK:  i - 4 SUM: 7
...
OK:  i - 60 SUM: 0
OK:  i - 61 SUM: 1
OK:  i - 62 SUM: 2
OK:  i - 63 SUM: 4
OK:  i - 64 SUM: 7

*/

vector<long long> remainders = { 0, 1 };

int get_period (long long n, long long m) {
    long long a = 0;
    long long b = 1;
    long long sum = a + b;

    for (long long i = 1; i < n + 2; ++i) {
        long long tmp = b;
        b = (a + b) % m;
        a = tmp;

        sum = (sum + b) % m;
        remainders.push_back(sum);

        if (i > 2 && remainders[2] == remainders[i] && remainders[1] == remainders[i - 1] && remainders[0] == remainders[i - 2]) {
            return i - 2;
        }
    }

    return n + 1;
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

int fibonacci_sum_period(long long n) {
    if (n <= 1)
        return n;

    int period = get_period(n, 10);

    int position_of_n = n % period;

//    std::cout << "n " << n << " period " << period << "\n";

    return remainders[n % period];
}

void test () {
    for (int i = 0; i < 100; ++i) {
        int r1 = fibonacci_sum_mod(i);
        int r2 = fibonacci_sum_period(i);
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
    std::cout << fibonacci_sum_period(n) << "\n";

}
