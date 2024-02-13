/*

Напишите функцию, которая принимает на вход целочисленную матрицу M (другими словами, просто двумерный целочисленный массив) размера rows x cols, и возвращает транспонированную матрицу M^T (тоже двумерный целочисленный массив) размера cols x rows. Если в M на пересечении i-ой строки и j-ого столбца стояло число x, то на пересечении  j-ой строки и i-ого столбца в матрице M^T  тоже будет стоять число x, или другими словами [][]=[][]M T [j][i]=M[i][j].Обратите внимание, что вам неизвестно, каким именно способом выделялась память для массива M. Выделять память под массив M T  можете любым удобным вам способом. Изменять исходную матрицу нельзя.Требования к реализации: при выполнении этого задания вы можете определять любые вспомогательные функции. Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.

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

int ** transpose(const int * const * m, unsigned rows, unsigned cols)
{
    int ** newArr = createArray2d(cols, rows);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            newArr[j][i] = m[i][j];
        }
    }

    delete [] m[0];
    delete [] m;

    return newArr;
}

int main() {
    int a = 3;
    int b = 5;

    int ** oldArr = createArray2d(a, b);

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            oldArr[i][j] = i * b + j;
        }
    }

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << oldArr[i][j] << " ";
        }
        cout << endl;
    }

    int ** newArr = transpose(oldArr, a, b);

    for (int i = 0; i < b; i++) {
        for (int j = 0; j < a; j++) {
            cout << newArr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}