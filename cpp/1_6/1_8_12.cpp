/*
Напишите программу, которая посимвольно читает из std::cin, пока не достигнет конца потока ввода, и заменяет несколько подряд идущих пробелов одним и выводит полученный результат в std::cout. Никаких других символов, кроме пробелов удалять не нужно. При выполнении задания вам не разрешается пользоваться дополнительной памятью, а именно: массивами, стандартными контейнерами и строками, даже если вы уже с ними знакомы. Вы можете определять любые вспомогательные функции, если они вам нужны.

Подсказка: прочтите внимательно степ про посимвольный ввод. Нулевой символ ('\0'), символ новой строки ('\n') и конец потока — это три разные вещи. Про то, как отловить конец потока —  написано в степе про посимвольный ввод.

Sample Input:
There are    a     lot  of    spaces  here

Sample Output:
There are a lot of spaces here
*/

#include <iostream>
using namespace std;

int main()
{
    char past = '\0';
    char c = '\0';
    while (cin.get(c)) {
        if (past == ' ' && c == ' ') {
            continue;
        }
        past = c;
        cout << c;
    }
    cout << endl;

	return 0;
}