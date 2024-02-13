#include <iostream>
using namespace std;

void foo(char) { std::cout << "char" << std::endl; }
void foo(signed char) { std::cout << "signed char" << std::endl; }
void foo(unsigned char) { std::cout << "unsigned char" << std::endl; }

float  square(float value) { return value * value; }
double square(float value) { return (double)value * value; }


int main () {

    // foo(97);
    // foo('a');

    double sq = square(2.0);

    cout << "sq " << sq << endl;

    return 0;
};