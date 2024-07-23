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
            if (stops[middle] < q) {
                while (stops[middle] < q && stops[middle + 1] < q)
                    middle += 1;
            } else {
                while (stops[middle] > q)
                    middle -= 1;
            }

            long long dl = std::abs(q - stops[middle]);
            long long dr = std::abs(stops[middle + 1] - q);

            if (dr < dl)
                result = middle + 1;
            else
                result = middle;

            break;
        };
    }

    return result + 1;
}

/*

-100 -20 -10

*/

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

5 3
1 3 7 20 21
4 1 19

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


1
3
4
4
5
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




*/
