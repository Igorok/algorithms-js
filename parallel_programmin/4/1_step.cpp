#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <omp.h>

using namespace std;

void parallelFor()
{
    printf("RAND_MAX %d \n", RAND_MAX);

    const long int n = 1000000;
    double* a = new double[n];
    double* b = new double[n];
    double* c = new double[n];

    for (int i = 0; i < n; ++i)
    {
        a[i] = rand() / RAND_MAX;
        b[i] = rand() / RAND_MAX;
    }

    double time = omp_get_wtime();

    #pragma omp parallel num_threads(4) shared(a, b, c)
    #pragma omp for
    for (int i = 0; i < n; ++i)
    {
        c[i] = a[i] + b[i];
    }

    printf("Time = %f \n", (omp_get_wtime() - time));
}

void forOrdered()
{
    int i, n;

    #pragma omp parallel private(i, n)
    {
        n = omp_get_thread_num();

        #pragma omp for ordered
        for (int i = 0; i < 5; ++i)
        {
            #pragma omp ordered
            {
                printf("ordered: Thread %d, iteration %d\n", n, i);
            }
        }


    }
}

void forCollapse()
{
    int j, k, jlast, klast;
    #pragma omp parallel num_threads(2)
    {
        #pragma omp for collapse(2) lastprivate(jlast, klast)
        for (k = 1; k <= 3; ++k) {
            for (j = 1; j <= 3; ++j) {
                printf(
                    "Thread %d k=%d j=%d \n",
                    omp_get_thread_num(),
                    k,
                    j
                );
                jlast = j;
                klast = k;
            }
        }

        #pragma omp single
        printf("klast = %d jlast = %d \n", klast, jlast);
    }
}

void forSchedule()
{
    int i;
    #pragma omp parallel num_threads(4) private(i)
    {
        // static, dynamic, guided
        #pragma omp for schedule (auto)
        for (i = 0; i < 200; ++i)
        {
            printf(
                "Thread %d solved iteration %d \n",
                omp_get_thread_num(),
                i
            );
            usleep(1);
        }
    }
}

int main () {
    parallelFor();

    return 0;
}
