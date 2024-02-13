/*

Конструкторов у структуры может быть несколько. Для строки может оказаться полезным заполняющий конструктор (например, чтобы создать строку пробелов). Заполняющий конструктор принимает число и символ, и создает строку с заданным количеством повторений переданного символа. Условия налагаемые на реализацию конструктора те же самые (в поле size размер без учета завершающего 0 символа, в поле str C-style строка, т.е. с завершающим 0 символом). Кроме конструктора в этой задаче вам нужно также реализовать и деструктор, который освободит выделенную память.
Требования к решению: в этом задании не нужно вводить или выводить что-либо, не нужно реализовывать функцию main. Для работы с памятью не используйте функции из cstdlib (malloc, calloc, realloc и free).

*/

#include <iostream>
#include <cstddef> // size_t
#include <cstring> // strlen, strcpy

using namespace std;


struct String {

    /* Реализуйте этот конструктор */
	String(size_t n, char c) {
        size = n;
        str = new char[n + 1];
        for (int i = 0; i < n; i++) {
            str[i] = c;
        }
        str[n] = '\n';
    }

    /* и деструктор */
	~String() {
        delete [] str;
    }


	size_t size;
	char *str;
};


int main () {
    String strObj(10, 'a');

    cout << "strObj.str " << strObj.str << " strObj.size " << strObj.size << endl;

    return 0;
}


