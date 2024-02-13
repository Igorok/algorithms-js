/*
Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел (Greatest Common Divisor, GCD).
Для этого воспользуйтесь следующими свойствами:
GCD(a, b) = GCD(b, a mod b)
GCD(0, a) = a
GCD(a, b) = GCD(b, a)
Требования к реализации: в данном задании запрещено пользоваться циклами. Вы можете заводить любые вспомогательные функции, если они вам нужны. Функцию main определять не нужно.
*/


#include <iostream>
using namespace std;

unsigned gcd(unsigned a, unsigned b)
{
    if (a >= b) {
        unsigned d = a % b;
        if (d == 0) {
            return b;
        } else {
            return gcd(d, b);
        }
    } else {
        unsigned d = b % a;
        if (d == 0) {
            return a;
        } else {
            return gcd(a, d);
        }
    }

    return 1;
}

int main()
{
    int a;
    int b;
    cin >> a >> b;


    unsigned div = gcd(a, b);

    cout << div << endl;

    return 0;
}
