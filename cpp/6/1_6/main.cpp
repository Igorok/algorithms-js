/*

Реализуйте шаблонную версию класса Array. Список всех операций, которые должен поддерживать класс Array, приведен в шаблоне кода.

#include <cstddef>

template <typename T>
class Array
{
    // Список операций:
    //
    // explicit Array(size_t size = 0, const T& value = T())
    //   конструктор класса, который создает
    //   Array размера size, заполненный значениями
    //   value типа T. Считайте что у типа T есть
    //   конструктор, который можно вызвать без
    //   без параметров, либо он ему не нужен.
    //
    // Array(const Array &)
    //   конструктор копирования, который создает
    //   копию параметра. Считайте, что для типа
    //   T определен оператор присваивания.
    //
    // ~Array()
    //   деструктор, если он вам необходим.
    //
    // Array& operator=(...)
    //   оператор присваивания.
    //
    // size_t size() const
    //   возвращает размер массива (количество
    //                              элементов).
    //
    // T& operator[](size_t)
    // const T& operator[](size_t) const
    //   две версии оператора доступа по индексу.
};

*/

#include <iostream>
#include <cstddef>
using namespace std;

template <typename T>
class Array
{
    size_t size_;
    T * data_;

    public:
        explicit Array(size_t size = 0, const T& value = T()):
        size_(size), data_(new T[size])
        {
            for (int i = 0; i < size; i++) {
                data_[i] = value;
            }
        }

        Array(const Array &copied) {
            if (this != &copied) {
                size_ = copied.size();
                data_ = new T[size_];
                for (int i = 0; i < size_; i++) {
                    data_[i] = copied[i];
                }
            }
        }

        ~Array() {
            delete [] data_;
        }

        Array& operator=(const Array &copied) {
            if (this != &copied) {
                size_ = copied.size();
                delete [] data_;
                data_ = new T[size_];
                for (int i = 0; i < size_; i++) {
                    data_[i] = copied[i];
                }
            }
            return *this;
        }

        size_t size() const {
            return size_;
        }

        T& operator[](size_t i) {
            return data_[i];
        }

        const T& operator[](size_t i) const {
            return data_[i];
        }
};

int main() {
    Array<int> ai_1(10);
    cout << "ai_1[2] " << ai_1[2] << endl;

    int * a_10 = new int[10];
    for (int i = 0; i < 10; i++) {
        a_10[i] = i;
    }
    cout << "a_10[2] " << a_10[2] << endl;

    Array<int> ai_2(10);
    for (int i = 0; i < 10; i++) {
        ai_2[i] = i;
    }
    cout << "ai_2[2] " << ai_2[2] << endl;

    ai_1 = ai_2;
    cout << "ai_1[2] " << ai_1[2] << endl;

    for (int i = 0; i < 10; i++) {
        ai_2[i] = i + 10;
    }
    cout << "ai_1[2] " << ai_1[2] << " ai_2[2] " << ai_2[2] << endl;

    Array<int> ai_3(ai_2);
    cout << "ai_3[2] " << ai_3[2] << endl;

}


