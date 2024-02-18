/*
BFS for 0, 1 weights.
*/

#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main () {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n);
    for (int i = 0; i < m; ++i) {
        int x, y, d;
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

    deque<int> q;
    vector<int> dist(n, -1);
    vector<int> pred(n, -1);

    q.push_back(start);
    dist[start] = 0;

    while (!q.empty()) {
        int current_vertex = q.front();
        q.pop_front();

        for (int i = 0; i < graph[current_vertex].size(); ++i) {
            int new_vertex = graph[current_vertex][i].first;
            int d = graph[current_vertex][i].second;

            if (dist[new_vertex] == -1 || dist[new_vertex] > dist[current_vertex] + d) {
                if (d == 0) {
                    q.push_front(new_vertex);
                } else {
                    q.push_back(new_vertex);
                }
                pred[new_vertex] = current_vertex;
                dist[new_vertex] = dist[current_vertex] + d;
            }
        }
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
