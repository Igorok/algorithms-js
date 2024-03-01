// g++ main.cpp -fopenmp -o build

#include <iostream>
#include <stdio.h>
#include <omp.h>
#include <string>

using namespace std;


void parallelShared ()
{
    int x = 0;
    #pragma omp parallel shared(x) num_threads(30)
    {
        x += 1;
    }

    cout << "x = " << x << endl;
}

void parallelPrivate ()
{
    int n = 1;
    printf("n в последовательной области, начало:%d\n", n);

    #pragma omp parallel private(n) num_threads(4)
    {
        printf("Значение в потоке, на входе:%d\n", n);
        n = omp_get_thread_num();
        printf("Значение в потоке, на выходе:%d\n", n);
    }

    printf("n в последовательной области, конец:%d\n", n);
}

void parallelFirstprivate ()
{
    int n = 1;
    printf("n в последовательной области, начало:%d\n", n);

    #pragma omp parallel firstprivate(n) num_threads(4)
    {
        printf("Значение в потоке, на входе:%d\n", n);
        n = omp_get_thread_num();
        printf("Значение в потоке, на выходе:%d\n", n);
    }

    printf("n в последовательной области, конец:%d\n", n);
}

void parallelReduction ()
{
    int x = 0;

    #pragma omp parallel reduction(+:x) num_threads(30)
    {
        x += 1;
    }

    cout << "x = " << x << endl;
}


int main(int argc, char *argv[])
{
    parallelReduction();

    return 0;
}