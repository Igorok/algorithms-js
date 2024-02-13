/*

Вам дан класс Foo:

struct Foo {
    void say() const { std::cout << "Foo says: " << msg << "\n"; }
protected:
    Foo(const char *msg) : msg(msg) { }
private:
    const char *msg;
};

Как видно, создатель класса не хотел чтобы его использовали и "спрятал" конструктор класса. Но вам очень нужен объект этого класса, чтобы передать его в функцию foo_says:

void foo_says(const Foo& foo) { foo.say(); }
В этом задании вам нужно реализовать функцию get_foo (сигнатура которой намерено не приводится в задании полностью, вам нужно подумать и вывести ее самостоятельно) так, чтобы следующий код компилировался и работал:

foo_says(get_foo(msg));
Где msg — произвольная C-style строка.

Требования к реализации: при выполнении задания вам разрешено вводить любые вспомогательные функции и классы. Запрещено изменять определение класса Foo или функции foo_says. Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.

*/

/* Этот код просто напоминание как выглядит класс Foo и функция foo_says.
 * Не нужно его расскоментировать и/или менять.
 *
 * #include <iostream>
 *
 * struct Foo {
 *     void say() const { std::cout << "Foo says: " << msg << "\n"; }
 * protected:
 *     Foo(const char *msg) : msg(msg) { }
 * private:
 *     const char *msg;
 * };
 *
 * void foo_says(const Foo &foo) { foo.say(); }
 *
 */

// Вам нужно определить функцию get_foo, как описано в задании,
// чтобы компилировался и работал как ожидается следующий код:
//
// foo_says(get_foo("Hello!"));




#include <iostream>
using namespace std;

// ?? get_foo(const char *msg) {

// }

struct Foo {
    void say() const { std::cout << "Foo says: " << msg << "\n"; }

    protected:
        Foo(const char *msg) : msg(msg) { }
    private:
        const char *msg;
};

void foo_says(const Foo& foo) {
    foo.say();
}

struct MyFoo: Foo {
    public:
        MyFoo(const char *msg_) : Foo(msg_) {
            size_t size = strlen(msg_);
            msg = new char[size + 1];
            for (size_t i = 0; i < size; i++) {
                msg[i] = msg_[i];
            }
            msg[size] = '\0';
        }
        ~MyFoo() {
            delete [] msg;
        }
    private:
        char *msg;

        size_t strlen(const char *str_)
        {
            size_t length = 0;
            while (*(str_ + length) != '\0') {
                length += 1;
            }
            return length;
        }
};

Foo get_foo(const char *msg) {
    const MyFoo myFoo(msg);
    return myFoo;
}

int main() {
    foo_says(get_foo("Hello!"));
}