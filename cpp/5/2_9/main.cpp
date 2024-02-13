/*

В этой задаче вам требуется реализовать оператор [] для уже известного вам класса String. Однако на этот раз оператор должен реализовывать нестандартное поведение: оператор нужно реализовать таким образом, чтобы для объекта str класса String можно было писать str[i][j] и это выражение возвращало подстроку начинающуюся в позиции i (считая с 0) и заканчивающуюся в позиции j (не включая).

Например:

String const hello("hello");
String const hell = hello[0][4]; // теперь в hell хранится подстрока "hell"
String const ell  = hello[1][4]; // теперь в ell хранится подстрока "ell"

Обратите внимание, что i может равняться j, в этом случае результатом должна быть пустая строка. Гарантируется, что i никогда не будет больше j, и они не будут выходить за пределы длины строки.
Требования к реализации: При выполнении задания вы можете создавать любые методы/конструкторы или даже структуры/классы, если они вам нужны. Реализовывать методы, которые уже объявленны в шаблоне, не нужно  они уже реализованы. При выполнении задания не вводите и не выводите что-либо. Реализовывать функцию main не нужно.


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

    /* Реализуйте оператор присваивания */
    String &operator=(const String &other) {
        if (this != &other) {
            size = other.size;
            delete [] str;

            str = new char[size + 1];
            for (size_t i = 0; i < size; i++) {
                str[i] = other.str[i];
            }
            str[size] = '\0';
        }
        return *this;
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


    operator[] (int i) {}


    size_t size;
    char *str;
};


int main () {
    String str1(new char[]{"hello world!"});

    String str2 = str1;

    cout << "str1 " << str1.str << " " << str1[6][11]<< endl;


    return 0;
}