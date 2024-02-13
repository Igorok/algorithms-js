/*
Реализуйте функцию getline, которая считывает поток ввода посимвольно, пока не достигнет конца потока или не встретит символ переноса строки ('\n'), и возвращает C-style строку с прочитанными символами.

Обратите внимание, что так как размер ввода заранее неизвестен, то вам нужно будет перевыделять память в процессе чтения, если в потоке ввода оказалось больше символов, чем вы ожидали.

Память, возвращенная из функции будет освобождена оператором delete[]. Символ переноса строки ('\n') добавлять в строку не нужно, но не забудьте, что в конце C-style строки должен быть завершающий нулевой символ.

Требования к реализации: при выполнении данного задания вы можете определять любые вспомогательные функции, если они вам нужны. Определять функцию main не нужно.
*/

#include <iostream>
using namespace std;


char *resize(const char *str, unsigned size, unsigned new_size)
{
    unsigned minSize = size > new_size ? new_size : size;
	char * n = new char[new_size];
    for (int i = 0; i < minSize; i++) {
        *(n + i) = *(str + i);
    }
    delete [] str;
    return n;
}

char *getline()
{
    int i = 0;
    int size = 1000;
    char *m = new char[size];
    char c = '\0';

    cout << "i " << i << endl;

    while (cin.get(c)) {
        if (c == '\n' || c == '\0') {
            break;
        }
        if (i == size - 2) {
            int newSize = size + 1000;
            m = resize(m, size, newSize);
            size = newSize;
        }
        m[i] = c;
        i++;
    }
    m[i] = '\0';

    cout << "i " << i << endl;


    return m;
}

int main () {
    char * n = getline();

    cout << n << endl;

    return 0;
}