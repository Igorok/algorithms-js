/*
g++ 9_path.cpp -o build
./9_path < 9.txt

В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

Входные данные
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.
Выходные данные
Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти).Если пути нет, нужно вывести -1.

Sample Input:
10
0 1 0 0 0 0 0 0 0 0
1 0 0 1 1 0 1 0 0 0
0 0 0 0 1 0 0 0 1 0
0 1 0 0 0 0 1 0 0 0
0 1 1 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 1 0 0 0 0 1 0 0
0 0 0 0 1 1 0 0 0 0
5 4

Sample Output:
2
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;


int getLength (vector<vector<int>> tree, int start, int end, int n) {
    vector<int> used(n, -1);
    vector<vector<int>> layers;

    layers.push_back({ start });
    int length = 0;
    used[start] = 1;

    while (!layers[length].empty()) {
        vector<int> layer = layers[length];
        layers.push_back({});

        for (int i = 0; i < layer.size(); i++) {
            int value = layer[i];
            if (value == end) {
                return length;
            }
            for (int j = 0; j < tree[value].size(); j++) {
                int child = tree[value][j];
                if (used[child] == 1) {
                    continue;
                }
                used[child] = 1;
                layers[length + 1].push_back(child);
            }
        }
        length += 1;
    }


    return -1;
}

int main()
{
    int n = -1;
    int s = -1;
    int e = -1;

    cin >> n;

    vector<vector<int>> tree(n, vector<int>(0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int val;
            cin >> val;
            if (val == 1) {
                tree[i].push_back(j);
            }
        }
    }

    cin >> s >> e;

    // for (int i = 0; i < n; i++) {
    //     cout << "i " << i << " j ";
    //     for (int j = 0; j < tree[i].size(); j++) {
    //         cout << tree[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    int length = getLength(tree, s-1, e-1, n);

    cout << length << endl;

    return 0;
};


/*

i 0 j 1
i 1 j 0 3 4 6
i 2 j 4 8
i 3 j 1 6
i 4 j 1 2 9
i 5 j 6 9
i 6 j 1 3 5
i 7 j 8
i 8 j 2 7
i 9 j 4 5
2

*/