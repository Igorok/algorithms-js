/*
The Bellman–Ford algorithm

Sample Input:
8 10 0

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

Sample Output:
2.75

*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int inf = (1 << 31) - 1;

int main () {
    int n = 0, m = 0, s = 0;
    cin >> n >> m;

    vector<vector<pair<int, int>>> g(n);

    for (int i = 0; i < m; ++i) {
        int f = 0, t = 0;
        int w = 0;
        cin >> f >> t >> w;
        --f;
        --t;

        g[f].push_back({t, w});
    }

    vector<int> r(n, inf);
    vector<bool> used(n, false);
    vector<int> p(n, -1);
    queue<int> q;

    q.push(s);
    r[s] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (auto e: g[cur]) {
            int to = e.first;
            int w = e.second;
            if (r[cur] + w < r[to]) {
                r[to] = r[cur] + w;
                p[to] = cur;
                q.push(to);
            }
        }
    }

    for (int i = 0; i < r.size(); ++i) {
        if (r[i] == inf) {
            cout << "30000" << " ";
        } else {
            cout << r[i] << " ";
        }
    }
    cout << endl;

    /*

    for (int i = 0; i < p.size(); ++i) {
        if (p[i] == -1) {
            continue;
        }
        cout << p[i] + 1 << " -> " << i + 1 << endl;
    }

    */

    return 0;
}
