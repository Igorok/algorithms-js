/*

Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

Входные данные
В первой строке содержатся три числа: N, S и F (1 <= N <= 100, 1 <= S, F <= N), где N – количество вершин графа, S – начальная вершина, а F – конечная. В следующих N строках вводится по N чисел, не превосходящих 100, – матрица смежности графа, где -1 означает отсутствие ребра между вершинами, а любое неотрицательное число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

Выходные данные
Требуется вывести искомое расстояние или -1, если пути между указанными вершинами не существует.

Sample Input:
3 2 1
0 1 1
4 0 1
2 1 0

Sample Output:
3

---

8 1 7
-1 1 0.5 -1 -1 -1 -1 -1
1 -1 -1 2 -1 -1 -1 1
0.5 -1 -1 3 -1 -1 -1 -1
-1 2 3 -1 -1 0.5 -1 0
-1 -1 -1 -1 -1 -1 1 0.25
-1 -1 -1 0.5 -1 -1 0.25 -1
-1 -1 -1 -1 1 0.25 -1 -1
-1 1 -1 0 0.25 -1 -1 -1
*/

#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

double bfsDouble(vector<vector<pair<int, double>>> &graph, int start, int finish) {
    vector<double> distance(graph.size(), -1);
    map<double, vector<int>> layers;

    distance[start] = 0;
    layers[0] = {start};

    // works like heap
    for (const auto& [dist, vertexes]: layers) {
        // all vertexes in distance - dist
        for (int i = 0; i < vertexes.size(); ++i) {
            // current vertex
            int vertex = vertexes[i];
            // all child vertexes
            for (int j = 0; j < graph[vertex].size(); ++j) {
                int new_vertex = graph[vertex][j].first;
                double d = graph[vertex][j].second;
                // if current distance of child vertex is more than distance from current vertex - update
                if (distance[new_vertex] == -1 || distance[new_vertex] > distance[vertex] + d) {
                    if (layers.find(distance[vertex] + d) == layers.end()) {
                        layers[distance[vertex] + d] = vector<int>();
                    }
                    distance[new_vertex] = distance[vertex] + d;
                    layers[distance[vertex] + d].push_back(new_vertex);
                }
            }
        }
    }

    return distance[finish];
}


void relax (vector<vector<pair<int, double>>> &graph, vector<double> &dist, int vertex) {
    for (int i = 0; i < graph[vertex].size(); ++i) {
        int new_vertex = graph[vertex][i].first;
        double d = graph[vertex][i].second;

        if (dist[new_vertex] > dist[vertex] + d) {
            dist[new_vertex] = dist[vertex] + d;
        }
    }
}

double dijkstraRelax (vector<vector<pair<int, double>>> &graph, int start, int finish) {
    vector<int> used(graph.size(), 0);
    vector<double> dist(graph.size(), 1e9);

    used[start] = 1;
    dist[start] = 0;

    relax(graph, dist, start);

    while (true) {
        int new_vertex = -1;
        double min_dist = 1e9;

        for (int i = 0; i < graph.size(); ++i) {
            if (used[i] == 0 && dist[i] < min_dist) {
                min_dist = dist[i];
                new_vertex = i;
            }
        }

        if (new_vertex == -1) {
            break;
        }

        relax(graph, dist, new_vertex);
        used[new_vertex] = 1;
    }

    // for (int i = 0; i < dist.size(); ++i) {
    //     cout << "i " << i+1 << " dist " << dist[i] << endl;
    // }


    return dist[finish] == 1e9 ? -1 : dist[finish];
}

double dijkstraSet(vector<vector<pair<int, double>>> &graph, int start, int finish) {
    set<pair<double, int>> layers;
    vector<double> distance(graph.size(), 1e9);

    distance[start] = 0;
    layers.insert({0, start});

    while (!layers.empty()) {
        int vertex = layers.begin()->second;
        layers.erase(layers.begin());

        for (int i = 0; i < graph[vertex].size(); ++i) {
            int new_vertex = graph[vertex][i].first;
            double d = graph[vertex][i].second;

            if (distance[new_vertex] > distance[vertex] + d) {
                layers.erase({distance[new_vertex], new_vertex});
                distance[new_vertex] = distance[vertex] + d;
                layers.insert({distance[new_vertex], new_vertex});
            }
        }
    }

    return distance[finish] == 1e9 ? -1 : distance[finish];
}

int main () {
    int n, s, f;
    cin >> n >> s >> f;
    --s;
    --f;

    vector<vector<pair<int, double>>> graph(n);
    for (int i = 0; i < n; ++i) {
        graph[i] = vector<pair<int, double>>();
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            double value;
            cin >> value;
            if (value != -1) {
                graph[i].push_back({j, value});
            }
        }
    }

    // cout << "n " << n << " s " << s << " f " << f << endl;
    // for (int i = 0; i < n; ++i) {
    //     cout << "i: " << i+1 << " ribs: " << endl;
    //     for (int j = 0; j < graph[i].size(); ++j) {
    //         cout << "vertex "<< graph[i][j].first+1 << " dist "<<graph[i][j].second << endl;
    //     }
    // }

    double dist = dijkstraSet(graph, s, f);
    cout << dist << endl;



    return 0;
}