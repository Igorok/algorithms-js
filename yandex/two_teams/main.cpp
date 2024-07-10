#include <iostream>
#include <string>
#include <vector>


int main()
{
	/*
	Для чтения входных данных необходимо получить их
	из стандартного потока ввода (stdin).
	Данные во входном потоке соответствуют описанному
	в условии формату. Обычно входные данные состоят
	из нескольких строк.

	Можно использовать несколько методов:
	* std::cin -- читает токены из потока;
	* std::getline() -- читает одну строку из потока;
	* scanf()/gets() -- C-функции для чтения из stdin.

	Чтобы прочитать из строки стандартного потока:
	* число -- int var; std::cin >> var;
	* строку -- std::string svar; std::cin >> svar;
	* массив чисел известной длины --
	std::vector<int> arr(len);
	for (size_t i = 0; i < arr.size(); ++i)
		std::cin >> arr[i];
	* последовательность слов до конца файла --
	std::vector<std::string> sarr;
	std::string word;
	while (std::cin >> word) {
		sarr.push_back(word);
	}

	Чтобы вывести результат в стандартный поток вывода (stdout),
	можно использовать поток std::cout.

	Возможное решение задачи "Вычислите сумму A+B":
	int a, b;
	std::cin >> a >> b;
	std::cout << a + b << std::endl;

    Ввод
	10
    8
    2

    Ввод
    3
    10
    3


    10 A
    8 B
    2 n

    Если решили n
    x * 2 = 10
    y * 2 = 8



    minX =



	*/

    int a, b, n;
	std::cin >> a >> b >> n;

	int maxPeople1 = a;

	int minPeople2 = int(b / n);
	if (b % n != 0) {
	    minPeople2 += 1;
	}

	std::cout << ((maxPeople1 > minPeople2) ? "YES" : "NO") << "\n";


	return 0;
}
