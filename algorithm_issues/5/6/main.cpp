/*

Last Digit of the Partial Sum of Fibonacci Numbers

Sample 1.
Input:
3 7
Output:
1

Sample 2.
Input:
10 10
Output:
5

*/

#include<iostream>
#include<vector>

using std::vector;

// I already know period is 60
vector<int> fibonacci_remainders = { 0, 1 };
void generate_fibonacci_remainders () {
    int a = 0;
    int b = 1;
    for (int i = 0; i < 70; ++i) {
        int tmp = b;
        b = (a + b) % 10;
        a = tmp;

        fibonacci_remainders.push_back(b);
    }

    /*
    for (int i = 0; i < 70; ++i) {
        std::cout << "i " << i << "fibonacci_remainders[i]" << fibonacci_remainders[i] << "\n";
    }
    */
}


int get_sum_remainder (long long n, long long m) {
    long long diff = m - n;

    int idA = n % 60;
    int idB = (idA + 1 > 59) ? 0 : (idA + 1);

    int a = fibonacci_remainders[idA];
    int b = fibonacci_remainders[idB];

    int sum = (a + b) % 10;
    vector <int> sumRemainder = { sum };
    int sumPeriod = m + 1;

    if (diff == 0) {
        return a;
    }

    for (int i = 1; i < diff; ++i) {
        int tmp = b;
        b = (a + b) % 10;
        a = tmp;

        sum = (sum + b) % 10;

        sumRemainder.push_back(sum);

        if (
            i > 10 &&
            sumRemainder[i-4] == sumRemainder[0] &&
            sumRemainder[i-3] == sumRemainder[1] &&
            sumRemainder[i-2] == sumRemainder[2] &&
            sumRemainder[i-1] == sumRemainder[3]
        ) {
            sumPeriod = i - 4;
            break;
        }

//        std::cout << "a " << a << " b " << b << "\n";
//        std::cout << "sum " << sum << "\n";
//        std::cout << "sumPeriod " << sumPeriod << "\n";
    }

    // get fibonacci numbers
    return sumRemainder[(diff - 1) % sumPeriod];
}

int main () {
    long long start, end;

    std::cin >> start >> end;

    generate_fibonacci_remainders();
    int sum = get_sum_remainder(start, end);

    std::cout << sum << "\n";

    return 0;
}


/*

i 0fibonacci_remainders[i]0
i 1fibonacci_remainders[i]1
i 2fibonacci_remainders[i]1
i 3fibonacci_remainders[i]2
i 4fibonacci_remainders[i]3
i 5fibonacci_remainders[i]5
i 6fibonacci_remainders[i]8
i 7fibonacci_remainders[i]3
i 8fibonacci_remainders[i]1
i 9fibonacci_remainders[i]4
i 10fibonacci_remainders[i]5
i 11fibonacci_remainders[i]9
i 12fibonacci_remainders[i]4
i 13fibonacci_remainders[i]3
i 14fibonacci_remainders[i]7
i 15fibonacci_remainders[i]0
i 16fibonacci_remainders[i]7
i 17fibonacci_remainders[i]7
i 18fibonacci_remainders[i]4
i 19fibonacci_remainders[i]1
i 20fibonacci_remainders[i]5
i 21fibonacci_remainders[i]6
i 22fibonacci_remainders[i]1
i 23fibonacci_remainders[i]7
i 24fibonacci_remainders[i]8
i 25fibonacci_remainders[i]5
i 26fibonacci_remainders[i]3
i 27fibonacci_remainders[i]8
i 28fibonacci_remainders[i]1
i 29fibonacci_remainders[i]9
i 30fibonacci_remainders[i]0
i 31fibonacci_remainders[i]9
i 32fibonacci_remainders[i]9
i 33fibonacci_remainders[i]8
i 34fibonacci_remainders[i]7
i 35fibonacci_remainders[i]5
i 36fibonacci_remainders[i]2
i 37fibonacci_remainders[i]7
i 38fibonacci_remainders[i]9
i 39fibonacci_remainders[i]6
i 40fibonacci_remainders[i]5
i 41fibonacci_remainders[i]1
i 42fibonacci_remainders[i]6
i 43fibonacci_remainders[i]7
i 44fibonacci_remainders[i]3
i 45fibonacci_remainders[i]0
i 46fibonacci_remainders[i]3
i 47fibonacci_remainders[i]3
i 48fibonacci_remainders[i]6
i 49fibonacci_remainders[i]9
i 50fibonacci_remainders[i]5
i 51fibonacci_remainders[i]4
i 52fibonacci_remainders[i]9
i 53fibonacci_remainders[i]3
i 54fibonacci_remainders[i]2
i 55fibonacci_remainders[i]5
i 56fibonacci_remainders[i]7
i 57fibonacci_remainders[i]2
i 58fibonacci_remainders[i]9
i 59fibonacci_remainders[i]1
i 60fibonacci_remainders[i]0
i 61fibonacci_remainders[i]1
i 62fibonacci_remainders[i]1
i 63fibonacci_remainders[i]2
i 64fibonacci_remainders[i]3
i 65fibonacci_remainders[i]5
i 66fibonacci_remainders[i]8
i 67fibonacci_remainders[i]3
i 68fibonacci_remainders[i]1
i 69fibonacci_remainders[i]4

*/
