/*
Напишите программу для вычисления целочисленного логарифма по основанию 2.
На вход программе в первой строке подается число T, далее следует T строк с тестами. Каждый тест состоит из одного целого положительного числа a[i]​ < 10^9 , для каждого a[i]​ нужно вывести на отдельной строке такое наибольшее число p, что 2^p <= a[i]​. Гарантируется, что a[i]​ >= 1 .
При решении задачи вы можете определять любые вспомогательные функции, если они вам нужны, более того рекомендуется вынести вычисление логарифма в отдельную функцию.
Ограничения: библиотеку cmath (и math.h) использовать запрещено.

Sample Input:
5
59218
50960
42043
42817
9998
1

Sample Output:
15
15
15
15
13
0
*/


#include <iostream>
using namespace std;

int getP (int a) {
    int p = 0;
    int accum = 1;
    while (accum < a) {
        accum *= 2;
        if (accum <= a) {
            p++;
        }

    }
    return p;
}

int main()
{
    int t;
    cin >> t;


    for (int i = 0; i < t; i++) {
        int a;
        cin >> a;
        int p = getP(a);
        cout << p << endl;
    }

    return 0;
}