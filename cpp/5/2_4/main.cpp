/*

Определите для класса Rational операторы сложения, вычитания, умножения и деления, так чтобы объекты типа Rational можно было складывать (вычитать, умножать и делить) не только друг с другом но и с целыми числами.

Требования к реализации: ваш код не должен вводить или выводить что-либо, реализовывать функцию main не нужно.

struct Rational
{
    Rational(int numerator = 0, int denominator = 1);

    void add(Rational rational);
    void sub(Rational rational);
    void mul(Rational rational);
    void div(Rational rational);

    void neg();
    void inv();
    double to_double() const;

    Rational& operator+=(Rational rational);
    Rational& operator-=(Rational rational);
    Rational& operator*=(Rational rational);
    Rational& operator/=(Rational rational);

    Rational operator-() const;
    Rational operator+() const;

private:
    int numerator_;
    int denominator_;
};

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

Rational operator+(Rational const & r, int i) {
    Rational newR(i);
    newR += r;
    return newR;
}
Rational operator+(int i, Rational const & r) {
    return r + i;
}
Rational operator+(Rational const & r1, Rational const & r2) {
    Rational newR(r1);
    newR += r2;
    return newR;
}

Rational operator-(Rational const & r, int i) {
    Rational newR(r);
    newR -= i;
    return newR;
}
Rational operator-(int i, Rational const & r) {
    Rational newR(i);
    newR -= r;
    return newR;
}
Rational operator-(Rational const & r1, Rational const & r2) {
    Rational newR(r1);
    newR -= r2;
    return newR;
}

Rational operator*(Rational const & r, int i) {
    Rational newR(i);
    newR *= r;
    return newR;
}
Rational operator*(int i, Rational const & r) {
    return r * i;
}
Rational operator*(Rational const & r1, Rational const & r2) {
    Rational newR(r1);
    newR *= r2;
    return newR;
}

Rational operator/(Rational const & r, int i) {
    Rational newR(r);
    newR /= i;
    return newR;
}
Rational operator/(int i, Rational const & r) {
    Rational newR(i);
    newR /= r;
    return newR;
}
Rational operator/(Rational const & r1, Rational const & r2) {
    Rational newR(r1);
    newR /= r2;
    return newR;
}


int main() {
    Rational r1(1, 2);
    Rational r2(5, 2);

    cout << "+" << endl;
    std::cout << "before "<< r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 + 1).to_double() << " "<< (1 + r1).to_double() << " "<< (r1 + r2).to_double() << std::endl;
    std::cout << "after "<< r1.to_double() << " " << r2.to_double() << std::endl;

    cout << "-" << endl;
    std::cout << "before "<< r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r2 - 1).to_double() << " "<< (1 - r1).to_double() << " "<< (r2 - r1).to_double() << std::endl;
    std::cout << "after "<< r1.to_double() << " " << r2.to_double() << std::endl;

}





