/*
Добавьте в класс String реализацию конструктора копирования. Инвариант класса остается тем же (в size хранится размер строки без завершающего 0 символа, str указывает на C-style строку, т. е. с завершающим нулевым символом).

Требования к реализации: вы можете заводить любые вспомогательные методы или функции, но не реализуйте заново методы из предыдущих заданий — они уже реализованы. При реализации не нужно вводить или выводить что-либо. Реализовывать main не нужно. Не используйте функции из cstdlib (malloc, calloc, realloc и free).


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
        for (size_t i = 0; i < n; i++) {
            str[i] = c;
        }
        str[n] = '\n';
    }

    /* Реализуйте конструктор копирования */
	String(const String &other) : size(other.size), str(new char(other.size + 1)) {
        this->copy(other.str);
    }

    /* и деструктор */
    ~String() {
        delete [] str;
    }


    /* Реализуйте этот метод. */
    void append(String &other) {
        char *newStr = new char[this->size + other.size + 1];
        for (size_t i = 0; i < this->size; i++) {
            newStr[i] = this->str[i];
        }
        for (size_t i = 0; i < other.size; i++) {
            newStr[this->size + i] = other.str[i];
        }
        this->size = this->size + other.size;
        newStr[this->size] = '\0';

        delete [] this->str;
        this->str = newStr;
    }

    size_t strlen(const char *str_)
    {
        size_t length = 0;
        while (*(str_ + length) != '\0') {
            length += 1;
        }
        return length;
    }

    void copy(const char *str_)
    {
        this->str = new char[this->size + 1];
        for (size_t i = 0; i < this->size; i++) {
            this->str[i] = str_[i];
        }
        this->str[this->size] = '\0';
    }


    size_t size;
    char *str;
};


int main () {
    String str1(new char[]{"aaaaaaaaaaaaaaaaaaaaaaaaaasd"});

    String str2(str1);

    cout << "str1 " << str1.str << endl;
    cout << "str2 " << str2.str << endl;


    return 0;
}