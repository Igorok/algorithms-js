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

using namespace std;


void relax (vector<vector<pair<int, double>>> &graph, vector<double> &dist, int vertex) {
    for (int i = 0; i < graph[vertex].size(); ++i) {
        int new_vertex = graph[vertex][i].first;
        double d = graph[vertex][i].second;
        if (dist[vertex] + d < dist[new_vertex]) {
            dist[new_vertex] = dist[vertex] + d;
        }
    }
}


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
    vector<int> used(n, 0);

    used[start] = 1;
    dist[start] = 0;

    relax(graph, dist, start);

    while (true) {
        double min_dist = 1e9;
        int new_vertex = -1;

        for (int i = 0; i < n; ++i) {
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

    for (int i = 0; i < n; ++i) {
        cout << i + 1 << " " << dist[i] << endl;
    }

    return 0;
}