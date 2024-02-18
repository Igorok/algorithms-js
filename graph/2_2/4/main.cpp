/*

BFS for fractional weights

*/

#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main () {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, double>>> graph(n);
    for (int i = 0; i < m; ++i) {
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

    cout << "n " << n << " m " << m << " start " << start << " end " << end << endl;

    vector<double> dist(n, -1);
    map<double, vector<int>> layers;
    vector<int> pred(n, -1);

    dist[start] = 0;
    layers[0] = {start};
    auto pointer = layers.begin();

    while (pointer != layers.end()) {
        double current_distance = pointer->first;
        for (int i = 0; i < pointer->second.size(); ++i) {
            int current_vertex = pointer->second[i];
            for (int j = 0; j < graph[current_vertex].size(); ++j) {
                int next_vertex = graph[current_vertex][j].first;
                double d = graph[current_vertex][j].second;

                if (dist[next_vertex] == -1 || dist[next_vertex] > dist[current_vertex] + d) {
                    if (layers.find(current_distance + d) == layers.end()) {
                        layers[current_distance + d] = vector<int> ();
                    }
                    layers[current_distance + d].push_back(next_vertex);
                    dist[next_vertex] = current_distance + d;
                    pred[next_vertex] = current_vertex;
                }
            }
        }
        ++pointer;
    }

    cout << "distance: " << endl;
    for (int i = 0; i < n; ++i) {
        cout << i + 1 << ": " << dist[i] << endl;
    }

    // path
    vector<int> path;
    int current_vertex = end;
    while (pred[current_vertex] != -1) {
        path.push_back(current_vertex);
        current_vertex = pred[current_vertex];
    }
    path.push_back(start);
    reverse(path.begin(), path.end());

    cout << "pred: " << endl;
    for (int i = 0; i < path.size(); ++i) {
        cout << path[i] + 1 << " ";
    }
    cout<< endl;

    return 0;
}