/*

Дан ориентированный граф. Определите, есть ли в нем цикл отрицательного веса.

Входные данные
В первой строке содержится число N (1 <= N <= 100) – количество вершин графа. В следующих N строках находится по N чисел – матрица смежности графа. Веса ребер по модулю меньше 100000. Если ребра нет, соответствующее значение равно 100000.

Выходные данные
В первой строке выведите "YES", если цикл существует, или "NO", в противном случае.

Sample Input 1:
1
100000

Sample Output 1:
NO

Sample Input 2:
1
0
Sample Output 2:
NO

Sample Input 3:
5
100000 100000 100000 5 100000
-20 100000 100000 100000 100000
100000 10 100000 100000 100000
100000 100000 100000 100000 7
100000 100000 -3 100000 100000

Sample Output 3:
YES

*/

#include <iostream>
#include <vector>

using namespace std;

const int maxVal = 100000;

struct edge {
    int f, t, w;
    edge(int _f, int _t, int _w): f(_f), t(_t), w(_w) {};
};

bool belmanFord(vector<edge> &edges, int n) {
    int edgesSize = edges.size();
    vector<int> distance(n, maxVal);

    distance[0] = 0;
    bool isBetter = false;

    for (int i = 0; i <= n; ++i) {
        isBetter = false;

        for (int j = 0; j < edgesSize; ++j) {
            edge e = edges[j];

            if (distance[e.f] == maxVal) {
                continue;
            }

            if (distance[e.t] > distance[e.f] + e.w) {
                distance[e.t] = distance[e.f] + e.w;
                isBetter = true;
            }
        }
    }

    // for (int i = 0; i < n; ++i) {
    //     cout << "i " << i+1 << " d " << distance[i] << endl;
    // }

    return isBetter;
}

int main () {
    int n = 0;
    cin >> n;

    vector<edge> edges;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int w = 0;
            cin >> w;
            if (w == maxVal) {
                continue;
            }
            edge e = edge(i, j, w);
            edges.push_back(e);

            // cout << "e.f " << e.f << " e.t " << e.t << " e.w " << e.w << endl;
        }
    }

    bool loop = belmanFord(edges, n);

    cout << (loop ? "YES" : "NO") << endl;

    return 0;
}