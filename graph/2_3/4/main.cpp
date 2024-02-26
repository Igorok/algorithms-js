/*
dijkstra algorithm

8 10

2 1 1
1 3 0.5
4 3 3
2 4 2
4 6 0.5
5 7 1
8 2 1
8 5 0.25
8 4 0
7 6 0.25

1 7

*/


#include <iostream>
#include <vector>
#include <set>

using namespace std;


int main () {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, double>>> graph(n);
    for (int i = 0; i < m; i++) {
        int x, y;
        double d;
        cin >> x >> y >> d;
        --x;
        --y;
        graph[x].push_back({y, d});
        graph[y].push_back({x, d});
    }

    int start, end;
    cin >> start >> end;
    --start;
    --end;

    vector<double> dist(n, 1e9);
    vector<int> pred(n, -1);
    dist[start] = 0;
    set<pair<double, int>> s;
    s.insert({0, start});

    while (!s.empty()) {
        int vertex = s.begin()->second;
        s.erase(s.begin());

        for (int i = 0; i < graph[vertex].size(); ++i) {
            int new_vertex = graph[vertex][i].first;
            double d = graph[vertex][i].second;

            if (dist[vertex] + d < dist[new_vertex]) {
                s.erase({dist[new_vertex], new_vertex});
                dist[new_vertex] = dist[vertex] + d;
                pred[new_vertex] = vertex;
                s.insert({dist[new_vertex], new_vertex});
            }
        }
    }


    for (int i = 0; i < n; ++i) {
        cout << i + 1 << " " << dist[i] << endl;
    }

    int parentVertex = end;
    while (parentVertex != -1) {
        cout << parentVertex + 1 << " ";
        parentVertex = pred[parentVertex];
    }
    cout << endl;

    return 0;
}