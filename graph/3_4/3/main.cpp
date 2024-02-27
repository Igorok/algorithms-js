/*
Bellman-Ford

No loop
6 6 0

0 1 1
1 2 1
0 5 1
2 3 1
3 1 1
3 4 1

Out
0 1 2 3 4 1

Loop
6 6 0

0 1 1
1 2 -1
0 5 1
2 3 -1
3 1 -1
3 4 1

Out
4
-1 3 1 2 3 0

*/

#include <iostream>
#include <vector>

using namespace std;

const int inf = (1 << 31) - 1;

struct edge {
    int f, t, w;
};

int main () {
    int n, m, v;
    cin >> n >> m >> v;

    vector<edge> e(m);
    vector<int> r(n, inf);

    for (int i = 0; i < m; ++i) {
        cin >> e[i].f >> e[i].t >> e[i].w;
    }

    r[v] = 0;
    vector<int> p(n, -1);
    int x = -1;

    for (int k = 0; k < n; ++k) {
        x = -1;

        for (int i = 0; i < m; ++i) {
            int f = e[i].f, t = e[i].t, w = e[i].w;

            if (r[f] == inf) continue;

            if (r[f] + w < r[t]) {
                r[t] = r[f] + w;
                p[t] = f;
                x = t;
            }
        }
    }

    cout << x << endl;

    for (int i = 0; i < n; ++i) {
        cout << r[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; ++i) {
        cout << p[i] << " ";
    }
    cout << endl;

    return 0;
}
