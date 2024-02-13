/*
Очень часто для работы со строками нам нужно сначала вычислить длину строки. Для C-style строк длина нигде явно не хранится, но её можно вычислить. Напишите функцию, которая вычисляет длину C-style строки. Учтите, что завершающий нулевой символ считать не нужно.

Требования к реализации: при выполнении этого задания вы можете создавать любые вспомогательные функции. Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.
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

int main()
{
    char str[]{ "asdsadasdasd" };
    int length = strlen(str);

    cout << "length " << length << endl;

    return 0;
}
