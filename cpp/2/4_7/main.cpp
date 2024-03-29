/*
Вам требуется реализовать функцию конкатенации (склейки) двух C-style строк. Функция конкатенации принимает на вход две C-style строки и дописывает вторую в конец первой так, чтобы первая строка представляла из себя одну C-style строку равную конкатенации двух исходных.

Не забудьте, что в результирующей строке должен быть только один нулевой символ — тот, что является маркером конца строки.

Гарантируется, что в первой строке достаточно памяти (т.е. она располагается в массиве достаточной длины), чтобы разместить конкатенацию обеих строк, но не больше.

Требования к реализации: при выполнении задания вы можете определять любые вспомогательные функции, если они вам нужны. Выводить или вводить что-либо не нужно. Функцию main определять не нужно.
*/



#include <iostream>
using namespace std;


unsigned strlen(const char *str)
{
    int length = 0;
    while (*(str + length) != '\0') {
        length += 1;
    }
    return length;
}

void strcat(char *to, const char *from)
{
    unsigned toLength = strlen(to);
    unsigned fromLength = strlen(from);

    for (int i = 0; i < fromLength; i++) {
        cout << *(from + i);
    }

    for (int i = 0; i < fromLength; i++) {
        *(to + toLength + i) = *(from + i);
    }
    *(to + toLength + fromLength) = '\0';
}

/*

asdsadasdasdasdsadasdas

*/
int main()
{
    char str1[]{ "asdsadasdasd" };
    char str2[]{ "asdsadasdasd" };
    strcat(str1, str2);

    for (int i = 0; i < (12 + 12); i++) {
        cout << i << *(str1 + i) << endl;
    }
    cout << endl;

    return 0;
}

