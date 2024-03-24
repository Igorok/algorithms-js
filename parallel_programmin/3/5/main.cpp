#include <stdio.h>
#include <omp.h>

void parallelNested ()
{
    int n;
    omp_set_nested(1);
    #pragma omp parallel private(n)
    {
        n = omp_get_thread_num();

        #pragma omp parallel
        {
            printf(
                "Part 1, thread %d - %d\n",
                n,
                omp_get_thread_num()
            );
        }
    }

    omp_set_nested(0);
    #pragma omp parallel private(n)
    {
        n = omp_get_thread_num();
        #pragma omp parallel
        {
            printf(
                "Part 2, thread %d - %d\n",
                n,
                omp_get_thread_num()
            );
        }
    }
}

void parallelCopyPrivate()
{
    int num;
    #pragma omp parallel num_threads(4) private(num)
    {
        num = omp_get_thread_num();

        printf("Before single num = %d \n", num);

        #pragma omp barrier
        #pragma omp single copyprivate(num)
        {
            printf("Enter number: ");
            scanf("%d", &num);
        }

        printf("After single num = %d \n", num);
    }
}

void parallelNowait ()
{
    #pragma omp parallel num_threads(4)
    {
        printf("Before single \n");

        #pragma omp single
        {
            printf("Insinde single \n");
        }

        printf("After single, always after single message \n");

        #pragma omp barrier

        printf("Before single nowait \n");

        #pragma omp single nowait
        {
            printf("Insinde single nowait\n");
        }

        printf("After single nowait. Can be before single message \n");
    }
}

void parallelMaster()
{
    int n;
    #pragma omp parallel num_threads(4) private(n)
    {
        n = 1;

        #pragma omp master
        {
            n = 2;
        }
        printf("First n: %d \n", n);

        #pragma omp barrier
        #pragma omp master
        {
            n = 3;
        }
        printf("Second n: %d \n", n);
    }
}

int main (int argc, char* argv[])
{
    parallelMaster();

    return 0;
}