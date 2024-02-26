/*

В стране N городов, некоторые из которых соединены между собой дорогами. Для того, чтобы проехать по одной дороге, требуется один бак бензина. В каждом городе бак бензина имеет разную стоимость. Вам требуется добраться из первого города в N-ый, потратив как можно меньшее денег. Покупать бензин впрок нельзя.

Входные данные
В первой строке вводится число N (1 <= N <= 100), в следующей строке идет N чисел, i-ое из которых задает стоимость бензина в i-ом городе (всё это целые числа из диапазона от 0 до 100). Затем идет число M – количество дорог в стране, далее идет описание самих дорог. Каждая дорога задается двумя числами – номерами городов, которые она соединяет. Все дороги двухсторонние (то есть по ним можно ездить как в одну, так и в другую сторону), между двумя городами всегда существует не более одной дороги, не существует дорог, ведущих из города в себя.

Выходные данные
Требуется вывести одно число – суммарную стоимость маршрута или -1, если добраться невозможно.

Sample Input:
9
5 3 4 5 7 9 1 2 5
12
1 3
1 2
2 4
3 4
2 5
4 5
4 6
6 9
4 7
7 8
5 8
8 9

Sample Output:
16

*/

#include <iostream>
#include <vector>

using namespace std;

void relax (vector<vector<int>> &graph, vector<int> &price, vector<int> &trip, int vertex) {
    for (int i = 0; i < graph[vertex].size(); ++i) {
        int new_vertex = graph[vertex][i];

        if (trip[new_vertex] > trip[vertex] + price[vertex]) {
            trip[new_vertex] = trip[vertex] + price[vertex];
        }
    }
}

int dijkstra (vector<vector<int>> &graph, vector<int> &price) {
    int size = graph.size();
    vector<int> used(size, 0);
    vector<int> trip(size, 1e9);
    int start = 0;
    int end = size - 1;

    trip[start] = 0;
    used[start] = 1;
    relax(graph, price, trip, start);

    while (true) {
        int new_vertex = -1;
        int min_price = 1e9;

        for (int i = 0; i < size; ++i) {
            if (used[i] == 0 && trip[i] < min_price) {
                new_vertex = i;
                min_price = trip[i];
            }
        }

        if (new_vertex == -1) {
            break;
        }

        relax(graph, price, trip, new_vertex);
        used[new_vertex] = 1;
    }


    // for (int i = 0; i < trip.size(); ++i) {
    //     cout << "i " << i + 1 << " " << trip[i] << endl;
    // }

    return trip[end] == 1e9 ? -1 : trip[end];
}

int main () {
    int n;
    cin >> n;

    vector<int> price(n, 0);
    for (int i = 0; i < n; ++i) {
        int p;
        cin >> p;
        price[i] = p;
    }

    vector<vector<int>> graph;
    for (int i = 0; i < n; ++i) {
        graph.push_back(vector<int>());
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; ++i) {
        int start, end;
        cin >> start >> end;
        --start;
        --end;
        graph[start].push_back(end);
        graph[end].push_back(start);
    }

    int p = dijkstra(graph, price);

    cout << p << endl;

    return 0;
}