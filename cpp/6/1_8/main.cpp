/*
Шаблонные классы можно наследовать. Реализуйте шаблонную структуру ValueHolder с одним типовым параметром T, унаследованную от интерфейса ICloneable. Интерфейс ICloneable содержит всего один виртуальный метод ICloneable* clone() const, который должен вернуть указатель на копию объекта, на котором он был вызван (объект должен быть создан в куче). Шаблон ValueHolder, как говорит его название, хранит всего одно значение (назовите его data_) типа T (для типа T определен конструктор копирования). Не делайте поле data_ закрытым (поэтому в данном случае мы явно пишем, что ValueHolder должна быть структурой).

struct ICloneable
{
	virtual ICloneable* clone() const = 0;
	virtual ~ICloneable() { }
};

// Шаблон ValueHolder с типовым параметром T,
// должен содержать одно открытое поле data_
// типа T.
//
// В шаблоне ValueHolder должен быть определен
// конструктор от одного параметра типа T,
// который инициализирует поле data_.
//
// Шаблон ValueHolder должен реализовывать
// интерфейс ICloneable, и возвращать указатель
// на копию объекта, созданную в куче, из метода
// clone.

template <typename T>
struct ValueHolder // дальше самостоятельно

*/

#include <iostream>
#include <cstddef>
using namespace std;

struct ICloneable
{
	virtual ICloneable* clone() const = 0;
	virtual ~ICloneable() { }
};

template <typename T>
struct ValueHolder {
    T * data_;

    ValueHolder() {}
    ~ValueHolder() {
        delete [] data_;
    }
    ValueHolder(const T& copied) {
        if (this != &copied) {
            data_ = new T[10];
            for (int i = 0; i < 10; i++) {
                data_[i] = copied.data_[i];
            }
        }
    }

    ValueHolder * clone(const T& copied) {
        return new ValueHolder(copied);
    };



};

int main () {
    ValueHolder<int> vh_1;
    vh_1.data_ = new int[10];
    for (int i = 0; i < 10; i++) {
        vh_1.data_[i] = i + 10;
    }
    cout << "vh_1.data_[2] " << vh_1.data_[2] << endl;

    ValueHolder<int> vh_2(vh_1);
    cout << "vh_2.data_[2] " << vh_2.data_[2] << endl;

    ValueHolder<int> vh_3;
    vh_3.data_ = new int[10];
    ValueHolder<int> vh_3.clone(vh_1);
    cout << "vh_3.data_[2] " << vh_3.data_[2] << endl;

    return 0;
}

















