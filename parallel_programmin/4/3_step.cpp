#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <omp.h>

using namespace std;

long fibonacci_1(long int n)
{

    long int a, b;
    if ((n == 1 || (n == 0))) {
        return n;
    } else {
        #pragma omp task shared(a)
        a = fibonacci_1(n-1);
        #pragma omp task shared(b)
        b = fibonacci_1(n - 2);
        #pragma omp taskwait
        return a + b;
    }
}

int main () {
    double start = omp_get_wtime();

    fibonacci_1(35);

    double end = omp_get_wtime();
    printf("Time: %f \n", (end - start));

    // Time: 1.195896
    //

    return 0;
}