/*

На шахматной доске NxN в клетке (x1, y1) стоит голодный шахматный конь. Он хочет попасть в клетку (x2, y2), где растет вкусная шахматная трава. Какое наименьшее количество ходов он должен для этого сделать?

Входные данные

На вход программы поступает  пять чисел: N, x1, y1, x2, y2 (5 <= N <= 20, 1 <= x1, y1, x2, y2 <= N). Левая верхняя клетка доски имеет координаты (1, 1), правая нижняя - (N, N).

Выходные данные

В первой строке выведите единственное число K - наименьшее необходимое число ходов коня.

Sample Input:
5
1 1
3 2

Sample Output:
1

*/

/*

  1 2 3 4 5
1 S 0 0 0 0
2 0 0 0 0 0
3 0 E 0 0 0
4 0 0 0 0 0
5 0 0 0 0 0

*/

#include <iostream>
#include <vector>
using namespace std;

bool checkCoord(int n, int x, int y) {
    if (x > 0 && x <= n && y > 0 && y <= n) {
        return true;
    }
    return false;
}

int getCount(int n, int x1, int y1, int x2, int y2) {
    vector<vector<int>> matrix(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> layers;

    layers.push_back(vector<int>());
    layers[0].push_back(x1);
    layers[0].push_back(y1);

    int i = 0;
    while (i < layers.size()) {
        // cout << "i " << i << " size " << layers.size() << endl;

        vector<int> layer = layers[i];
        if (layer.empty()) {
            break;
        }

        layers.push_back(vector<int>());
        int j = 0;
        while (j < layer.size()) {
            int stepX = layer[j];
            int stepY = layer[j + 1];
            j += 2;

            // cout << "stepX " << stepY << " stepY " << stepY << endl;

            if (matrix[stepX][stepY] == 1) {
                continue;
            }

            matrix[stepX][stepY] = 1;
            if (x2 == stepX && y2 == stepY) {
                return i;
            }

            if (checkCoord(n, stepX + 1, stepY + 2)) {
                layers[i + 1].push_back(stepX + 1);
                layers[i + 1].push_back(stepY + 2);
            }
            if (checkCoord(n, stepX + 1, stepY - 2)) {
                layers[i + 1].push_back(stepX + 1);
                layers[i + 1].push_back(stepY - 2);
            }
            if (checkCoord(n, stepX - 1, stepY + 2)) {
                layers[i + 1].push_back(stepX - 1);
                layers[i + 1].push_back(stepY + 2);
            }
            if (checkCoord(n, stepX - 1, stepY - 2)) {
                layers[i + 1].push_back(stepX - 1);
                layers[i + 1].push_back(stepY - 2);
            }

            if (checkCoord(n, stepX + 2, stepY + 1)) {
                layers[i + 1].push_back(stepX + 2);
                layers[i + 1].push_back(stepY + 1);
            }
            if (checkCoord(n, stepX + 2, stepY - 1)) {
                layers[i + 1].push_back(stepX + 2);
                layers[i + 1].push_back(stepY - 1);
            }
            if (checkCoord(n, stepX - 2, stepY + 1)) {
                layers[i + 1].push_back(stepX - 2);
                layers[i + 1].push_back(stepY + 1);
            }
            if (checkCoord(n, stepX - 2, stepY - 1)) {
                layers[i + 1].push_back(stepX - 2);
                layers[i + 1].push_back(stepY - 1);
            }
        }
        ++i;
    }

    return 0;
}

int main() {
    int n;
    cin >> n;

    int x1;
    int y1;
    cin >> x1 >> y1;

    int x2;
    int y2;
    cin >> x2 >> y2;

    cout << getCount(n, x1, y1, x2, y2) << endl;

    return 0;
}