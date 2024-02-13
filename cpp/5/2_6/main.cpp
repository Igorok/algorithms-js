/*

Еще одна важная группа операторов, которые полезно реализовать для класса рациональных чисел — это операторы сравнения. Реализуйте операторы <, <=, >, >=, ==, != для класса Rational так, чтобы можно было сравнивать объекты класса Rational не только друг с другом, но и с целыми числами.

При решении задания не используйте метод to_double, он введен в класс, в первую очередь, для удобства тестирования. Вы можете определять любые вспомогательные методы или функции если необходимо.

Требования к реализации: ваш код не должен вводить или вводить что-либо, реализовывать функцию main не нужно.

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

    int getNum() const {
        return numerator_;
    }
    int getDenom() const {
        return denominator_;
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

bool operator< (Rational const & r1, Rational const & r2) {
    if (r1.getNum() < r2.getNum()) {
        return true;
    } else if (r1.getNum() > r2.getNum()) {
        return false;
    } else {
        return r1.getDenom() < r2.getDenom();
    }
}
bool operator> (Rational const & r1, Rational const & r2) {
    return r2 < r1;
}
bool operator== (Rational const & r1, Rational const & r2) {
    return !(r1 < r2) && !(r1 > r2);
}
bool operator!= (Rational const & r1, Rational const & r2) {
    return !(r1 == r2);
}
bool operator<= (Rational const & r1, Rational const & r2) {
    return !(r1 > r2);
}
bool operator>= (Rational const & r1, Rational const & r2) {
    return !(r1 < r2);
}



int main() {
    Rational r1(1, 2);
    Rational r2(5, 2);

    cout << "==" << endl;
    std::cout << "before "<< r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 < r2) << " " << (r1 < 1) << " " << (r1 < 0.1) << std::endl;
    std::cout << "after "<< r1.to_double() << " " << r2.to_double() << std::endl;

    cout << "==" << endl;
    std::cout << "before "<< r1.to_double() << " " << r2.to_double() << std::endl;
    std::cout << (r1 == 0.5) << " "<< (r1 == 1) << " "<< (r1 == r2) << std::endl;
    std::cout << "after "<< r1.to_double() << " " << r2.to_double() << std::endl;


}