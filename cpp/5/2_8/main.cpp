/*

Добавьте в класс Rational оператор приведения к double. Все операторы из предыдущих заданий отсутствуют и реализовывать их не нужно. Метод to_double можно использовать в этом задании.

Важное замечание: добавлять оператор преобразования к double в класс Rational не самая удачная идея, например, потому, что при таком преобразовании может происходить потеря точности. Эта задача дана исключительно с целью ознакомления с правильным порядком перегрузки таких операторов.

Требования к реализации: ваш код не должен вводить или вводить что-либо, реализовывать функцию main не нужно.

*/


#include <iostream>
using namespace std;


struct Rational
{
    Rational(int numerator = 0, int denominator = 1): numerator_(numerator), denominator_(denominator) {};

    void add(Rational rational);
    void sub(Rational rational);
    void mul(Rational rational);
    void div(Rational rational);

    void neg();
    void inv();

    double to_double() const {
        return (double)numerator_ / (double)denominator_;
    };

    operator double const () const {
        if (this) {
            return this->to_double();
        }
        return 0;
    }

private:
    int numerator_;
    int denominator_;
};

int main() {
    Rational r1(1, 3);

    cout << r1.to_double() << " " << (double)r1 << endl;


    return 0;
}
