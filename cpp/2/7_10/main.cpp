/*

Реализуйте функцию swap_min, которая принимает на вход двумерный массив целых чисел, ищет в этом массиве строку, содержащую наименьшее среди всех элементов массива значение, и меняет эту строку местами с первой строкой массива.
Подумайте, как обменять строки массива, не обменивая элементы строк по-отдельности.
Требования к реализации: при выполнении этого задания вы можете определять любые вспомогательные функции. Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.

*/


#include <iostream>
using namespace std;

int ** createArray2d (unsigned a, unsigned b) {
    int ** m = new int * [a];
    m[0] = new int [a * b];
    for (int i = 1; i != a; i++) {
        m[i] = m[i - 1] + b;
    }
    return m;
}

void swap_min(int *m[], unsigned rows, unsigned cols)
{
    int min = m[0][0];
    int minRow = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (m[i][j] < min ) {
                min = m[i][j];
                minRow = i;
            }
        }
    }

    if (minRow != 0) {
        int * tmp = m[0];
        m[0] = m[minRow];
        m[minRow] = tmp;
    }
}


int main () {
    unsigned a = 3;
    unsigned b = 5;

    int ** oldArr = createArray2d(a, b);

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            oldArr[i][j] = (a - i - 1) * b + j;
        }
    }

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << oldArr[i][j] << " ";
        }
        cout << endl;
    }

    swap_min(oldArr, a, b);

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << oldArr[i][j] << " ";
        }
        cout << endl;
    }


    return 0;
}