/*

Реализованные в предыдущих заданиях конструкторы и деструктор берут на себя работу по управлению ресурсами. Теперь можно дополнить структуру String различными полезными методами.

Для работы со строками можно придумать множество полезных методов (подумайте, какие методы пригодились бы вам, и чего вам не хватает для их реализации). Примером такого метода может послужить метод append — он добавляет копию строки-аргумента в конец текущей строки (т.е. в конец строки, у которой он был вызван).

String s1("Hello,");
String s2(" world!");

s1.append(s2); // теперь s1 хранит "Hello, world!"
Ваша задача реализовать метод append.

При выполнении задания будьте аккуратны при работе с памятью — при вызове метода не должно возникать утечек памяти. Кроме того, не забудьте, что size хранит размер без учета завершающего 0 символа.

Требования к реализации: при реализации вы можете заводить любые вспомогательные функции и методы. В шаблоне вы увидите объявления уже известных вам конструкторов и деструкторов, реализовывать их заново не нужно, они уже реализованы. Вводить или выводить что-либо не нужно. Реализовывать main не нужно. Для работы с памятью не используйте функции из cstdlib (malloc, realloc, calloc и free).

Кроме того, ваша реализация должна корректно работать в следующем тесте:

String s("Hello");
s.append(s); // теперь s хранит "HelloHello"


*/

#include <iostream>
#include <cstddef> // size_t
#include <cstring> // strlen, strcpy

using namespace std;

struct String {
    /* Реализуйте этот конструктор */
    String(const char *str = "") {
        size = this->strlen(str);
        this->copy(str);
    }
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


    /* Реализуйте этот метод. */
    void append(String &other) {
        char *newStr = new char[this->size + other.size + 1];
        for (int i = 0; i < this->size; i++) {
            newStr[i] = this->str[i];
        }
        for (int i = 0; i < other.size; i++) {
            newStr[this->size + i] = other.str[i];
        }
        this->size = this->size + other.size;
        newStr[this->size] = '\0';

        delete [] this->str;
        this->str = newStr;
    }

    size_t size;
    char *str;

    private:
        unsigned strlen(const char *str)
        {
            int length = 0;
            while (*(str + length) != '\0') {
                length += 1;
            }
            return length;
        }

        void copy(const char *str)
        {
            this->str = new char[this->size + 1];
            for (int i = 0; i < this->size; i++) {
                this->str[i] = str[i];
            }
            this->str[this->size] = '\0';
        }
};


int main () {
    char str1[] = "Hello";
    String strObj1(str1);

    cout << "strObj1.str " << strObj1.str << " strObj1.size " << strObj1.size << endl;

    char str2[] = "World!";
    String strObj2(str2);

    cout << "strObj2.str " << strObj2.str << " strObj2.size " << strObj2.size << endl;

    strObj1.append(strObj2);

    cout << "strObj1.str " << strObj1.str << " strObj1.size " << strObj1.size << endl;

    return 0;
}