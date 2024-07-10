#include <iostream>
#include <string>
#include <vector>

using std::vector;

long long search (vector<long long> &stops, long long q) {
    if (q < stops[0]) return 1;
    if (q > stops[stops.size() - 1]) return stops.size();


    int start = 0;
    int end = stops.size();

    int result = -1;
    while (true) {
        int middle = (int)((end + start) / 2);

        if (stops[middle] == q) {
            result = middle;
            end = middle - 1;
        }

        if (q > stops[middle]) {
            start = middle + 1;
        }
        if (q < stops[middle]) {
            end = middle - 1;
        }

        if (start > end) {
            if (stops[result] != q) {
                if (q < stops[middle]) {
                    for (int i = middle; i > 0; --i) {
                        if (q < stops[middle] && q > stops[middle - 1]) {
                            result = middle - 1;
                            break;
                        }
                    }
                } else {
                    for (int i = middle; i < stops.size(); ++i) {
                        if (q > stops[middle] && q < stops[middle + 1]) {
                            result = middle;
                            break;
                        }
                    }
                }
            }

            break;
        };
    }

    return result + 1;
}


int main()
{
    int n, k;
    std::cin >> n >> k;

    vector<long long> stops;

    for (int i = 0; i < n; ++i) {
        long long val;
        std::cin >> val;
        stops.push_back(val);
    }

    for (int i = 0; i < k; ++i) {
        long long val;
        std::cin >> val;

        std::cout << search(stops, val) << "\n";
    }


	return 0;
}

/*

3 2
1 3 5
4 1

Попробуй вот такой:

6 7
1 1 3 5 7 7
1 2 3 4 5 6 7
Должно быть:
1
2
3
3
4
4
5
---
1
2
3
3
4
4
5

---

7 6
-99 -99 -99 0 99 99 99
-99 -88 0 10 98 99
1
3
4
4
5
5
---
1
3
4
4
4
5




7 10
1 1 3 5 7 7 10
0 1 2 3 4 5 6 7 8 100
Вывод: 1 1 2 3 3 4 4 5 6 7


1
1
2
3
3
4
4
5
6
7


7 6
-99 -99 -99 0 99 99 99
-88 -1 0 1 88 100
3 4 4 4 5 7

7 7
-99 -99 -99 0 99 99 99
-100 -88 -1 0 1 88 100
1 3 4 4 4 5 7


10 5
-100 -98 -97 -96 0 5 7 10 12 15
-99 -43 -1 3 2
Ответ:
1 5 5 6 5


---

Можешь сказать, какой у тебя вывод для такого кейса? (задача 423 про автобусы и остановки)
7 4
1 3 3 3 5 5 5
3 4 5 6
По логике моего решения для этих запросов надо вывести 2, 2, 5, 5 (на отдельной строке каждое число офк)



у меня прошли все тесты, на этом варианте мой код выводит 2, 4, 5, 7















*/
