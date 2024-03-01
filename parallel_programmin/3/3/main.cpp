// g++ main.cpp -fopenmp -o build

#include <stdio.h>

/*
int sub (int max)
{
    #pragma omp parallel
    {
        int n = 30;
        // invalid exit from OpenMP structured block
        if (n > max) return 1;
    }

    return 0;
}
*/

void parallelPrint() {
    printf("Последовательная область 1\n");

    #pragma omp parallel num_threads(4)
    {
        printf("Параллельная область\n");
    }

    printf("Последовательная область 2\n");
}

int main(int argc, char *argv[])
{
    parallelPrint();
    // sub(20);

    return 0;
}