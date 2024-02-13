/*

Вам дан класс Rational, который описывает рациональное число. В нем определены методы add, sub, mul и div, которые прибавляют к нему число, отнимают число, умножают на число и делят на число соответственно. Кроме того в нем определен метод neg, который меняет знак на противоположный.

Вам нужно определить операторы +=, -=, *=, /= для класса Rational так, чтобы они могли принимать в качестве аргументов и объекты типа Rational и целые числа. Кроме того вам необходимо определить операторы унарного минуса и плюса для класса Rational.

Требования к реализации: ваш код не должен вводить или вводить что-либо, реализовывать функцию main не нужно. Кроме того, нельзя (это совершенно не нужно) использовать динамическую память или подключать какие-либо библиотеки.

*/

#include <iostream>
using namespace std;

struct Rational
{
    Rational(int numerator = 0, int denominator = 1) : numerator_(numerator), denominator_(denominator) {};

    void add(Rational rational) {
        numerator_ = numerator_ * rational.denominator_ + rational.numerator_ * denominator_;
        denominator_ *= rational.denominator_;
    }

    void sub(Rational rational) {
        numerator_ = numerator_ * rational.denominator_ - rational.numerator_ * denominator_;
        denominator_ *= rational.denominator_;
    }

    void mul(Rational rational) {
        numerator_ *= rational.numerator_;
        denominator_ *= rational.denominator_;
    }

    void div(Rational rational) {
        numerator_ *= rational.denominator_;
        denominator_ *= rational.numerator_;
    }

    void neg() {
        numerator_ = -numerator_;
    }

    void inv() {}

    double to_double() const {
        return numerator_ / (double) denominator_;
    }

    Rational operator+ () const {
        return Rational(this->numerator_, this->denominator_);
    }
    Rational operator- () const {
        Rational newThis(this->numerator_, this->denominator_);
        newThis.neg();
        return newThis;
    }
    Rational & operator -=(Rational const& r) {
        this->sub(r);
        return *this;
    }
    Rational & operator -=(int i) {
        this->sub(Rational(i));
        return *this;
    }
    Rational & operator +=(Rational const & r) {
        this->add(r);
        return *this;
    }
    Rational & operator +=(int i) {
        this->add(Rational(i));
        return *this;
    }
    Rational & operator *=(Rational const & r) {
        this->mul(r);
        return *this;
    }
    Rational & operator *=(int i) {
        this->mul(Rational(i));
        return *this;
    }
    Rational & operator /=(Rational const & r) {
        this->div(r);
        return *this;
    }
    Rational & operator /=(int i) {
        this->div(Rational(i));
        return *this;
    }

private:
    int numerator_;
    int denominator_;
};


int main() {
    Rational r1(1, 2);
    Rational r2(5, 2);

    cout << "int" << endl;
    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 += r2).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 += 5).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 -= r2).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 -= 5).to_double() << std::endl;

     std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 *= r2).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 *= 5).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 /= r2).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 /= 5).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (-r1).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (+r1).to_double() << std::endl;

    std::cout << r1.to_double() << " " << r2.to_double() << std::endl;


}