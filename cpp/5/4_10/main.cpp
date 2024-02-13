/*
https://courses.cs.washington.edu/courses/cse326/02wi/unix/g++.html

Compiling multiple files
Most likely, you will be compiling separate modules and linking them into a single executable. Here's the basic idea: compile each .C file into a .o file, then link the .o files (along with any libraries) into an executable. Of course, one of these .C files has to define the main() or else the linker will complain. Suppose we have main.C, foo.C and bar.C and want to create an executable fubar, and suppose further that we need the math library:
% g++ -c -o foo.o foo.C
% g++ -c -o main.o main.C
% g++ -c -o bar.o bar.C
% g++ -o fubar foo.o main.o bar.o -lm


g++ -c main.cpp -o ./build/main.o
g++ -c first.cpp -o ./build/first.o
g++ -c second.cpp -o ./build/second.o
g++ -c third.cpp -o ./build/third.o

g++ -o ./build/program ./build/main.o ./build/first.o ./build/second.o ./build/third.o -lm

https://stepik.org/lesson/535/step/6?unit=858

Если что:
Создаете файлы:
foo.hpp
functions.hpp
main.cpp
firts.cpp
second.cpp
third.cpp

Компилируете:
g++ -c main.cpp -o ./build/main.o
g++ -c first.cpp -o ./build/first.o
g++ -c second.cpp -o ./build/second.o
g++ -c third.cpp -o ./build/third.o

Линкуете:
g++ -o ./build/program ./build/main.o ./build/first.o ./build/second.o ./build/third.o -lm

Запускаете:
./build/program
*/

#include "functions.hpp"

int main() {
    first();
    second();
    third();
    return 0;
}
