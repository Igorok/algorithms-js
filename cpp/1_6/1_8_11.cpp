/*
Напишите программу для решения квадратных уравнений вида ax^2 + bx + c = 0 (относительно x).
На вход программа получает три целых числа: a ,b и c, соответственно. При этом гарантируется, что a != 0. На вывод программа должна вывести два вещественных корня уравнения, разделённые пробелом. Если вещественных корней нет, то программа должна вывести строку "No real roots". Если у уравнения имеется только один корень (кратный корень), то программа должна вывести его дважды. Порядок вывода корней не важен. Ничего, кроме этого, выводить не нужно. Для вычислений с плавающей точкой используйте тип double. При выполнении задания вам может оказаться полезной функция sqrt из заголовочного файла cmath.Замечание: после того, как вы сдадите это задание, попробуйте подумать, как изменилась бы ваша программа, если бы мы не гарантировали, что a != 0.
*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int a, b, c;

    cin >> a >> b >> c;

    int d = b * b - 4 * a * c;
    int a2 = 2*a;

    if (d > 0) {
        double sqrD = sqrt(d);
        double x1 = (sqrD - b) / a2;
        double x2 = (-1 * sqrD - b) / a2;
        cout << x1 << " " << x2 << endl;
    } else if (d == 0) {
        double x = -1 * (b / a2);
        cout << x << " "  << x << endl;
    } else {
        cout << "No real roots" << endl;
    }

    return 0;
}